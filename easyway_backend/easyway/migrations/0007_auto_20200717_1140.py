# Generated by Django 2.2.2 on 2020-07-17 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easyway', '0006_hotel_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='address',
        ),
        migrations.RemoveField(
            model_name='activities',
            name='geolocation',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='address',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='geolocation',
        ),
        migrations.RemoveField(
            model_name='rent_car',
            name='address',
        ),
        migrations.RemoveField(
            model_name='rent_car',
            name='geolocation',
        ),
    ]
