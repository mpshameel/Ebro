# Generated by Django 3.1.7 on 2021-05-15 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0049_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.BigIntegerField(blank=True, default='1', null=True),
        ),
    ]
