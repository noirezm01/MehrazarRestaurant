# Generated by Django 4.2.5 on 2023-10-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.CharField(max_length=500, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='food',
            name='photo',
            field=models.ImageField(upload_to='foods/', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='food',
            name='rate',
            field=models.IntegerField(default=0, verbose_name='امتیاز'),
        ),
    ]
