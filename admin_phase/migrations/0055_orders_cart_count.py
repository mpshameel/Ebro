# Generated by Django 3.1.7 on 2021-05-21 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0054_delete_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='cart_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]