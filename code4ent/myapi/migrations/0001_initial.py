# Generated by Django 3.1.3 on 2020-12-09 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='My_API_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(max_length=55)),
                ('api_details', models.CharField(max_length=55)),
            ],
        ),
    ]
