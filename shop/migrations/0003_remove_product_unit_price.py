# Generated by Django 5.0.3 on 2024-03-17 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_unit_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='unit_price',
        ),
    ]
