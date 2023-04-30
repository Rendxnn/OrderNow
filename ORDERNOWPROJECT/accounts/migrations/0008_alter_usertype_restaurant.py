# Generated by Django 4.2 on 2023-04-30 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_initial'),
        ('accounts', '0007_alter_usertype_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='restaurant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant'),
        ),
    ]
