# Generated by Django 2.2.2 on 2020-07-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic=False
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_title', models.TextField(max_length=20)),
                ('days', models.DateTimeField()),
                ('opening_hours', models.DateTimeField()),
                ('age', models.IntegerField()),
                ('max_persons', models.IntegerField()),
                ('discount_per_person', models.SmallIntegerField(verbose_name=50)),
                ('group_discount_per_person', models.SmallIntegerField(verbose_name=50)),
            ],
        ),
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='User', max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phonenumber', models.IntegerField()),
                ('AccountNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_of_guests', models.IntegerField(verbose_name=8)),
                ('No_of_bedrooms', models.IntegerField(verbose_name=8)),
                ('No_of_beds', models.IntegerField(verbose_name=8)),
                ('No_of_baths', models.IntegerField(verbose_name=8)),
                ('No_of_toilets', models.IntegerField(verbose_name=8)),
                ('more_details', models.TextField(max_length=200)),
                ('checkin', models.TimeField(auto_now_add=True)),
                ('checkout', models.TimeField(auto_now_add=True)),
                ('discount_per_person', models.SmallIntegerField(verbose_name=50)),
                ('group_discount_per_person', models.SmallIntegerField(verbose_name=50)),
            ],
        ),
        migrations.CreateModel(
            name='rent_car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=200)),
                ('more_details', models.TextField(max_length=200)),
                ('place_available', models.TextField(verbose_name=20)),
                ('discount_per_person', models.SmallIntegerField(verbose_name=50)),
            ],
        ),
    ]
