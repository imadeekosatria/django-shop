# Generated by Django 4.1.7 on 2023-03-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_halaman_created_at_halaman_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='visitor',
            field=models.IntegerField(default=None),
        ),
    ]
