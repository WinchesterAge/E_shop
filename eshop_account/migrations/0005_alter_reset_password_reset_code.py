# Generated by Django 4.0 on 2022-06-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_account', '0004_reset_password_delete_reset_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reset_password',
            name='reset_code',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
