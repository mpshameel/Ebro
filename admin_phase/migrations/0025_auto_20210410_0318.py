# Generated by Django 3.1.7 on 2021-04-09 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0024_auto_20210410_0317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_attachments',
            old_name='job',
            new_name='product',
        ),
    ]
