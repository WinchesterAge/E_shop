# Generated by Django 4.0 on 2022-05-18 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('eshop_products', '0014_alter_product_slug'),
        ('eshop_favlist', '0004_remove_favorite_list_details_list_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name': 'لیست کابر',
                'verbose_name_plural': 'لیست های کاربران',
            },
        ),
        migrations.CreateModel(
            name='Favorite_list_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_favlist.favorite_list')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_products.product')),
            ],
            options={
                'verbose_name': 'محصول درون لیست',
                'verbose_name_plural': 'محصولات درون لیست',
            },
        ),
    ]