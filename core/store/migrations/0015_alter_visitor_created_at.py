# Generated by Django 4.1.7 on 2023-03-31 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_visitor_remove_product_visitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
