# Generated by Django 2.2.2 on 2020-07-07 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('easyway', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='address',
            field=django_google_maps.fields.AddressField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='activities',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='easyway.customers'),
        ),
        migrations.AddField(
            model_name='activities',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='activity_title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='easyway.activities'),
        ),
        migrations.AddField(
            model_name='customers',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile/'),
        ),
        migrations.AddField(
            model_name='customers',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hotel',
            name='activity_title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='easyway.activities'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='address',
            field=django_google_maps.fields.AddressField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rent_car',
            name='activity_title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='easyway.activities'),
        ),
        migrations.AddField(
            model_name='rent_car',
            name='add_photos',
            field=models.ImageField(null=True, upload_to='cars/'),
        ),
        migrations.AddField(
            model_name='rent_car',
            name='address',
            field=django_google_maps.fields.AddressField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rent_car',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(blank=True, max_length=100, null=True),
        ),
    ]