# Generated by Django 4.1.7 on 2023-04-06 05:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0010_product_recieved_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
