from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import gettext_lazy as _

# Create your models here.

# User table
class User(AbstractUser):
    phone = models.CharField(_('Phone'), max_length=15, blank=True, null=True)
    username = models.CharField(_('Username'), unique=True,max_length=15, blank=True, null=True)
    email = models.EmailField(_('Email Address'), null=True, blank=True)
    password = models.CharField(_('Password'), max_length=155, null=True, blank=True)
    otp = models.CharField(_('otp'), max_length=10, blank=True, null=True)
    is_otp_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True, db_index=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'app_user'
        verbose_name = 'app_user'
        verbose_name_plural = 'app_user'
        managed = True

    def __str__(self):
        return f"{self.username}"

# for demo weather data
class Weather(models.Model):
    country = models.CharField(_('Shop Name'),max_length=50,null=True,blank=True)
    city = models.CharField(_('Address'),max_length=155,null=True,blank=True)
    temperature = models.CharField(max_length=25,null=True,blank=True)
    monday = models.CharField(null=False, blank=True, max_length=150)
    tuesday = models.CharField(null=False, blank=True, max_length=150)
    wednesday = models.CharField(null=False, blank=True, max_length=150)
    thursday = models.CharField(null=False, blank=True, max_length=150)
    friday = models.CharField(null=False, blank=True, max_length=150)
    saturday = models.CharField(null=False, blank=True, max_length=150)
    sunday = models.CharField(null=False, blank=True, max_length=150)
    date = models.DateField(auto_now=True, db_index=True)

    class Meta:
        db_table = 'weather_data'
        verbose_name = 'weather_data'
        verbose_name_plural = 'weather_data'
        managed = True

    def __str__(self):
        return f"{self.country}"
