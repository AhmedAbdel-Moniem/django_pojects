# Generated by Django 3.0.7 on 2020-06-05 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='department',
            field=models.TextField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='train',
            name='name',
            field=models.TextField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='train',
            name='roll_no',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='train',
            name='stud_class',
            field=models.TextField(default='', max_length=30),
        ),
    ]
