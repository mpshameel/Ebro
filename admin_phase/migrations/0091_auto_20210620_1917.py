# Generated by Django 3.1.7 on 2021-06-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0090_auto_20210619_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='feedback',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='notification',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
