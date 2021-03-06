# Generated by Django 4.0 on 2022-01-24 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=30)),
                ('fax', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=80)),
            ],
            options={
                'verbose_name': 'تنظیم سابت',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
    ]
