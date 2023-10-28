from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone


class Reservation(models.Model):
    name = models.CharField(_('نام و نام خانوادگی'), max_length=200)
    email = models.EmailField(_('آدرس الکترونیکی'), max_length=200)
    phone = models.CharField(_('شماره موبایل'), max_length=11)
    number = models.IntegerField(_('تعداد نفرات'))
    date = models.DateField(_('تاریخ'))
    time = models.TimeField(_('زمان'))

    def __str__(self):
        return self.phone+' '+self.name
