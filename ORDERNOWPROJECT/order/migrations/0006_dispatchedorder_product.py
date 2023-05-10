# Generated by Django 4.2 on 2023-05-10 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_initial'),
        ('order', '0005_remove_dispatchedorder_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispatchedorder',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='restaurants.product'),
            preserve_default=False,
        ),
    ]
