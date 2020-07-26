# Generated by Django 2.2.2 on 2020-07-13 11:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    atomic=False
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('easyway', '0003_easyway'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='activities',
            new_name='activity',
        ),
        migrations.RenameModel(
            old_name='customers',
            new_name='customer',
        ),
    ]
