# Generated by Django 4.0 on 2022-01-26 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_order', '0003_rename_user_order_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'سبد خرید', 'verbose_name_plural': 'سبد های خرید'},
        ),
        migrations.AlterModelOptions(
            name='order_detail',
            options={'verbose_name': 'جزییات خرید', 'verbose_name_plural': 'جزییات خرید ها'},
        ),
    ]
