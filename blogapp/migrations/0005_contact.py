# Generated by Django 3.0.6 on 2020-06-11 01:06

from django.db import migrations, models
import django.utils.timezone
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20200611_0438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('number', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('message', models.CharField(max_length=1000)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
    ]
