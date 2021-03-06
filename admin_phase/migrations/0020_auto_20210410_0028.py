# Generated by Django 3.1.7 on 2021-04-09 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_phase', '0019_auto_20210409_0125'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='attachments',
            new_name='deal_attachments',
        ),
        migrations.CreateModel(
            name='jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.CharField(blank=True, max_length=100, null=True)),
                ('job_name', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.BigIntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('job_type', models.CharField(blank=True, max_length=100, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=100, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='deals/deals_pic')),
                ('details', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='job_attachments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(blank=True, null=True, upload_to='deals/deals_attachments')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_phase.deals')),
            ],
        ),
    ]
