from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create UserProfile when User is created"""
    if created:
        # Determine role based on user permissions
        if instance.is_superuser:
            role = 'admin'
        elif instance.is_staff:
            role = 'staff'
        else:
            role = 'student'
        
        # Create UserProfile
        UserProfile.objects.create(
            user=instance, 
            role=role,
            is_active=instance.is_active
        )
          # Note: Member record creation is now handled by the registration form
        # to ensure proper data is saved, not default values