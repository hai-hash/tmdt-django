# Generated by Django 3.1.7 on 2021-06-01 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_rename_order_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='process',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='orders',
            name='statusstr',
            field=models.CharField(default='Chờ xác nhận', max_length=100),
        ),
    ]
