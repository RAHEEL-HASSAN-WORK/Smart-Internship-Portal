# accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from students.models import StudentProfile
from companies.models import CompanyProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'student':
            StudentProfile.objects.create(user=instance)
        elif instance.role == 'company':
            CompanyProfile.objects.create(user=instance)
