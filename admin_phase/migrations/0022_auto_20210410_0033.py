# Generated by Django 3.1.7 on 2021-04-09 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_phase', '0021_auto_20210410_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_attachments',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_phase.jobs'),
        ),
    ]