# Generated by Django 3.1.3 on 2020-11-22 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=True, default=True, max_digits=2),
            preserve_default=False,
        ),
    ]