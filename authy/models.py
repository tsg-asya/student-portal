from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import os


class User(AbstractUser):
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username


def user_directory_path(instance, filename):
    profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)
    return profile_pic_name


class Degree_Batch(models.Model):
    title = models.CharField(max_length=30, verbose_name='Title')
    full_title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
    gender = models.CharField(
        ('Gender'), choices=GENDER, max_length=7, default=GENDER[0][0])
    slug = models.SlugField(primary_key=True, null=False)
    enrollment_no = models.CharField(max_length=25, blank=True)
    contact = models.CharField(max_length=20, default='')
    local_address = models.CharField(max_length=15, blank=True)
    city_state = models.CharField(max_length=15, blank=True)
    guardian_name = models.CharField(max_length=20, blank=True)
    guardian_contact_no = models.CharField(max_length=20, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True, blank=True)
    picture = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)
    degree_batch = models.ForeignKey(
        Degree_Batch, related_name='degree_batch', on_delete=models.SET_NULL, null=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username + '-' + self.enrollment_no


# signals

# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)
#     instance.student.save()

# post_save.connect(create_or_update_user_profile, sender=User)
