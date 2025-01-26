# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    رقم وكالة = models.IntegerField(null=True, blank=True)
    مدينة = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Agency(models.Model):

    #__Agency_FIELDS__
    إسم = models.CharField(max_length=255, null=True, blank=True)
    عنوان = models.CharField(max_length=255, null=True, blank=True)

    #__Agency_FIELDS__END

    class Meta:
        verbose_name        = _("Agency")
        verbose_name_plural = _("Agency")


class Hajez(models.Model):

    #__Hajez_FIELDS__
    تاريخ = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Hajez_FIELDS__END

    class Meta:
        verbose_name        = _("Hajez")
        verbose_name_plural = _("Hajez")



#__MODELS__END
