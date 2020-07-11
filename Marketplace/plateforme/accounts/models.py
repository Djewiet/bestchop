from django.db import models
from django.conf import  settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=False)
    email = models.EmailField(_('Email Adress'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']#, 'first_name', 'last_name']

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Man'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=5, blank=True)
    first_name = models.CharField(max_length=80,blank=True)
    last_name = models.CharField(max_length=80,blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Man')
    phone = models.CharField(max_length=20,blank=True)
    date_of_birth = models.CharField(max_length=20,blank=True)  #DateField(blank=T)
    address = models.CharField(max_length=255,blank=True)
    country = models.CharField(max_length=50,blank=True)
    city = models.CharField(max_length=50,blank=True)
    zip = models.CharField(max_length=5,blank=True)
    created = models.DateTimeField(auto_now_add=True,blank=True)
    updated = models.DateTimeField(auto_now=True,blank=True)


