# Generated by Django 4.2 on 2023-05-10 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_dispatchedorder_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispatchedorder',
            name='order_id',
        ),
    ]