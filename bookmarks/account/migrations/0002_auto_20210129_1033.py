# Generated by Django 3.0.11 on 2021-01-29 10:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profle',
            new_name='Profile',
        ),
    ]
