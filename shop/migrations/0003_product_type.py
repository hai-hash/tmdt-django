# Generated by Django 3.2.3 on 2021-05-31 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210530_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(default='', max_length=100),
        ),
    ]