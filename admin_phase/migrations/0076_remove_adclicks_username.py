# Generated by Django 3.1.7 on 2021-06-08 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0075_auto_20210608_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adclicks',
            name='username',
        ),
    ]
