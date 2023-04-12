# Generated by Django 4.1.7 on 2023-03-30 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default=None, max_length=100)),
                ('city', models.CharField(default=None, max_length=100)),
                ('address', models.CharField(default=None, max_length=100)),
                ('phone', models.IntegerField(default=None, max_length=100)),
                ('zip', models.IntegerField(default=None, max_length=100)),
                ('instagram', models.URLField(default=None)),
                ('facebook', models.URLField(default=None)),
                ('wa_message', models.CharField(default=None, max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
