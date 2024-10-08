# Generated by Django 5.1 on 2024-08-10 17:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0009_auto_20240808_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='converted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
