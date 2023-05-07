# Generated by Django 4.2 on 2023-05-06 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.table')),
            ],
        ),
    ]