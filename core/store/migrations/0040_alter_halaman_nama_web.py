# Generated by Django 4.1.7 on 2023-04-04 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0039_alter_halaman_address_alter_halaman_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='halaman',
            name='nama_web',
            field=models.CharField(default='Store', max_length=100, unique=True),
        ),
    ]
