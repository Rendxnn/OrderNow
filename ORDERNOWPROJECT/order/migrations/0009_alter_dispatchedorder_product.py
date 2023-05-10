# Generated by Django 4.2 on 2023-05-10 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_initial'),
        ('order', '0008_alter_dispatchedorder_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatchedorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.product'),
        ),
    ]
