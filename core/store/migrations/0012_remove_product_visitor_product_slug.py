# Generated by Django 4.1.7 on 2023-03-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_contact_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='visitor',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
