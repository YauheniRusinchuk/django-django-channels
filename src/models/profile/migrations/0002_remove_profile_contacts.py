# Generated by Django 2.2.4 on 2019-08-19 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='contacts',
        ),
    ]
