from django.db import models

# Create your models here.

from django.db import models
from accounts.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    education = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
