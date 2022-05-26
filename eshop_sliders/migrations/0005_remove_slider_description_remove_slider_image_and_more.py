# Generated by Django 4.0 on 2022-01-30 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0013_product_views'),
        ('eshop_sliders', '0004_slider_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='description',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='image',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='title',
        ),
        migrations.AlterField(
            model_name='slider',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eshop_products.product'),
        ),
    ]