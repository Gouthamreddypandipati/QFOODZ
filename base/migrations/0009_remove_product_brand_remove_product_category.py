# Generated by Django 4.1.3 on 2022-11-30 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_review_createdat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
