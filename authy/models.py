from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class User(AbstractUser):
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
    enrollment_no = models.CharField(max_length=25, blank=True)
    contact = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=15, blank=True)
    guardian_name = models.CharField(max_length=20, blank=True)
    guardian_contact_no = models.CharField(max_length=20, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


# signals

# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)
#     instance.student.save()

# post_save.connect(create_or_update_user_profile, sender=User)
