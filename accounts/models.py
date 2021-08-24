from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    AbstractUserFields = username, first/last_name, email, is_staff, is_active,
    date_joined, objects
    """

    age = models.PositiveIntegerField(null=True, blank=True)
    bio_text = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True, default='blank_profile.png', upload_to='images/profiles/')
    #active_projects = models.ForeignKey(Project, on_delete=models.SET_NULL(), null=True, blank=True, default=None)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)

