import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals  import post_save
from django.dispatch  import receiver
from  backend.storage_backends import PrivateMediaStorage
from  .managers import UserManager
from django.contrib.auth.models import AbstractUser
from sorl.thumbnail import ImageField

def get_image_path(instance, filename):
    return os.path.join('images', str(instance.id), filename)

# Create your models here.
class Users(AbstractUser):
    email = models.EmailField(blank=True, max_length=254, unique=True)
    username = models.CharField(blank=True, max_length=150, unique=True)
    Usertypes = (
        ('eprocure-admin', 'eprocure-admin'),
        ('client', 'client'),
        ('supplier', 'supplier')
    )
    user_type = models.CharField(choices=Usertypes, max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

# User Profile Model


class Profile(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user',db_index=True)
    profile_pic = ImageField(
        upload_to= get_image_path, default="", storage= PrivateMediaStorage(), blank=True, null=True
    )
    phone_no = models.CharField(max_length=13, blank=True, null=True)
    id_number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

#Signals for Automatically  creating a user profile on  user signup
@receiver(post_save, sender=Users)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
            Profile.objects.create(user=instance)


@receiver(post_save, sender=Users)
def save_user_profile(sender, instance, **kwargs):
    u_obj = Users.objects.filter(id=instance.id).first()
    Profile.objects.get(user=u_obj).save()

