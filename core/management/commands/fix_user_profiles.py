from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import UserProfile
from student.models import Member

class Command(BaseCommand):
    help = 'Fix users without profiles and create missing Member records'

    def handle(self, *args, **options):
        fixed_count = 0
        
        # Find users without UserProfile
        users_without_profile = User.objects.filter(profile__isnull=True)
        
        self.stdout.write(f"Found {len(users_without_profile)} users without profiles")
        
        for user in users_without_profile:
            # Determine role based on user permissions
            if user.is_superuser:
                role = 'admin'
            elif user.is_staff:
                role = 'staff'
            else:
                role = 'student'
            
            # Create UserProfile
            profile, profile_created = UserProfile.objects.get_or_create(
                user=user,
                defaults={'role': role}
            )
            
            if profile_created:
                self.stdout.write(f"✅ Created UserProfile for {user.username} (role: {role})")
                fixed_count += 1
            
            # Create Member record for students
            if role == 'student':
                member, member_created = Member.objects.get_or_create(
                    user=user,
                    defaults={
                        'member_id': f"STU{user.id:05d}",
                        'name': f"{user.first_name} {user.last_name}".strip() or user.username,
                        'email': user.email,
                        'phone_number': '',
                        'address': '',
                        'gender': 'M',
                        'age': 18,
                        'date_of_birth': '2000-01-01',
                        'max_books': 3,
                        'max_reservations': 2,
                        'is_active': user.is_active
                    }
                )
                
                if member_created:
                    self.stdout.write(f"✅ Created Member record for {user.username} (ID: {member.member_id})")
                    fixed_count += 1
        
        # Also check for students without Member records
        student_profiles = UserProfile.objects.filter(role='student')
        for profile in student_profiles:
            if not hasattr(profile.user, 'member_profile'):
                member, member_created = Member.objects.get_or_create(
                    user=profile.user,
                    defaults={
                        'member_id': f"STU{profile.user.id:05d}",
                        'name': f"{profile.user.first_name} {profile.user.last_name}".strip() or profile.user.username,
                        'email': profile.user.email,
                        'phone_number': '',
                        'address': '',
                        'gender': 'M',
                        'age': 18,
                        'date_of_birth': '2000-01-01',
                        'max_books': 3,
                        'max_reservations': 2,
                        'is_active': profile.user.is_active
                    }
                )
                
                if member_created:
                    self.stdout.write(f"✅ Created missing Member record for student {profile.user.username}")
                    fixed_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully fixed {fixed_count} user records')
        )
