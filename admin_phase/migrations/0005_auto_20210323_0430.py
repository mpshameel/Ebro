# Generated by Django 3.1.7 on 2021-03-22 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0004_auto_20210323_0424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='refferalcode',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='usertype',
        ),
    ]
