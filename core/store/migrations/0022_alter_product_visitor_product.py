# Generated by Django 4.1.7 on 2023-04-01 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_alter_halaman_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='visitor_product',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]