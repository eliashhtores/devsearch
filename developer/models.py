from django.db import models
from django.contrib.auth.models import User
import uuid


class Developer(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        upload_to='profiles/', blank=True, null=True, default='profiles/user-default.png')
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    social_stackoverflow = models.CharField(
        max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
