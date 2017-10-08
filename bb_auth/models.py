from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    timezone = models.CharField(max_length=50, default=settings.TIME_ZONE)
    
    def __str__(self):
        return "User Profile for user {}".format(self.user.username)
        
        