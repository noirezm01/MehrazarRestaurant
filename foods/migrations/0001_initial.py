# Generated by Django 4.2.5 on 2023-10-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=50, verbose_name='توضیحات')),
                ('rate', models.IntegerField(verbose_name='امتیاز')),
                ('price', models.IntegerField()),
                ('time', models.IntegerField(verbose_name='زمان لازم')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('photo', models.ImageField(upload_to='foods/')),
            ],
        ),
    ]
