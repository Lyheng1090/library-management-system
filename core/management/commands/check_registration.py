from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from student.models import Member
from core.models import UserProfile

class Command(BaseCommand):
    help = 'Clean up orphaned records and fix registration issues'

    def handle(self, *args, **options):
        self.stdout.write('Starting cleanup...')
        
        # Find users without Member profiles (students should have them)
        student_profiles = UserProfile.objects.filter(role='student')
        self.stdout.write(f'Found {student_profiles.count()} student profiles')
        
        missing_members = 0
        for profile in student_profiles:
            try:
                member = profile.user.member_profile
            except Member.DoesNotExist:
                missing_members += 1
                self.stdout.write(f'User {profile.user.username} has no Member profile')
        
        # Find members with empty addresses
        empty_addresses = Member.objects.filter(address__in=['', None])
        self.stdout.write(f'Found {empty_addresses.count()} members with empty addresses')
        
        for member in empty_addresses:
            self.stdout.write(f'  - {member.name} ({member.member_id}): address="{member.address}"')
        
        # Find UserProfiles without corresponding Members
        orphaned_profiles = 0
        for profile in student_profiles:
            if not hasattr(profile.user, 'member_profile'):
                orphaned_profiles += 1
        
        self.stdout.write(f'Summary:')
        self.stdout.write(f'  - Total student profiles: {student_profiles.count()}')
        self.stdout.write(f'  - Missing member profiles: {missing_members}')
        self.stdout.write(f'  - Empty addresses: {empty_addresses.count()}')
        self.stdout.write(f'  - Orphaned profiles: {orphaned_profiles}')
        
        self.stdout.write(self.style.SUCCESS('Cleanup analysis complete!'))
