# Generated by Django 4.1.3 on 2022-12-07 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_product_brand_remove_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='delivery_time',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
