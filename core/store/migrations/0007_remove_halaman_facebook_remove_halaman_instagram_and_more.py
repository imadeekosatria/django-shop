# Generated by Django 4.1.7 on 2023-03-30 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_halaman_facebook_halaman_instagram_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='halaman',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='halaman',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='halaman',
            name='wa_message',
        ),
        migrations.RemoveField(
            model_name='halaman',
            name='whatsapp',
        ),
    ]