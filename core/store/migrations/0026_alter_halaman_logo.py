# Generated by Django 4.1.7 on 2023-04-01 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_alter_product_visitor_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='halaman',
            name='logo',
            field=models.ImageField(blank=True, default=None, upload_to='profile'),
        ),
    ]
