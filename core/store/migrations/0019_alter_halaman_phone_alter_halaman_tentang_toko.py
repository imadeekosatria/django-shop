# Generated by Django 4.1.7 on 2023-03-31 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_halaman_email_alter_contact_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='halaman',
            name='phone',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='halaman',
            name='tentang_toko',
            field=models.TextField(default=None, max_length=500),
        ),
    ]
