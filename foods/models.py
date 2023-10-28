from django.db import models
from django.utils.translation import gettext as _


class Food(models.Model):
    FOOD_TYPE = [
        ('breakfast', 'صبحانه'),
        ('lunch', 'ناهار'),
        ('drinks', 'نوشیدنی'),
        ('dinner', 'شام')
    ]
    name = models.CharField(_('نام'), max_length=100)
    description = models.CharField(_('توضیحات'), max_length=500)
    rate = models.IntegerField(_('امتیاز'), default=0)
    price = models.IntegerField(_('قیمت'))
    time = models.IntegerField(_('زمان لازم'))
    pub_date = models.DateField(_('تاریخ انتشار'), auto_now=False, auto_now_add=True)
    photo = models.ImageField(_('عکس'), upload_to='foods/')
    type_food = models.CharField(_('نوع غذا'), max_length=10, choices=FOOD_TYPE, default='lunch')

    def __str__(self):
        return self.name
