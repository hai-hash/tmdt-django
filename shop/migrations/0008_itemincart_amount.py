# Generated by Django 3.2.3 on 2021-06-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210601_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemincart',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
