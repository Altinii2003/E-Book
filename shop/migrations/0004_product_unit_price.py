# Generated by Django 5.0.3 on 2024-03-17 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_product_unit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit_price',
            field=models.FloatField(default=0.0),
        ),
    ]