# Generated by Django 4.2.11 on 2024-04-24 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('choucair_testing_app', '0002_products_product_image_alter_products_create_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='id',
            new_name='product_id',
        ),
    ]