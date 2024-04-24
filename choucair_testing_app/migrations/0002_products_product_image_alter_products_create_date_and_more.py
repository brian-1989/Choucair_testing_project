# Generated by Django 4.2.11 on 2024-04-24 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choucair_testing_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_image',
            field=models.ImageField(default='', upload_to='product image/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='create_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='update_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]