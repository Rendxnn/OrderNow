# Generated by Django 4.2 on 2023-04-28 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('grammage', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='products/product_images')),
            ],
        ),
    ]