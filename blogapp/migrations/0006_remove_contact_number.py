# Generated by Django 3.0.6 on 2020-06-12 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='number',
        ),
    ]
