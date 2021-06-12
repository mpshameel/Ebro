# Generated by Django 3.1.7 on 2021-05-09 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0042_products_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.BigIntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wallet',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]