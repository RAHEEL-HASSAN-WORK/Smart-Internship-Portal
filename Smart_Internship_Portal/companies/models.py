from django.db import models

# Create your models here.

from django.db import models
from accounts.models import User

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True)

    def __str__(self):
        return self.company_name
