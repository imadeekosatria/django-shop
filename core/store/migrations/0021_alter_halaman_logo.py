# Generated by Django 4.1.7 on 2023-04-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_alter_halaman_address_alter_halaman_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='halaman',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
