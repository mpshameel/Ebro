# Generated by Django 3.1.7 on 2021-05-09 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0043_auto_20210509_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.BigIntegerField(blank=True, default='1', null=True),
        ),
    ]
