from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from post.models import Post
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    profile_image = models.ImageField(upload_to="profile_images/", verbose_name="Profile Image", null=True, blank=True)
    favourite_posts = models.ManyToManyField(Post)
    
    def image_url(self):
        MEDIA_URL = settings.MEDIA_URL
        if self.profile_image:
            return MEDIA_URL + self.profile_image.name

        default_image_path = MEDIA_URL + f"default_profile_images/{self.user.username[0]}.png"

        return default_image_path

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, User)