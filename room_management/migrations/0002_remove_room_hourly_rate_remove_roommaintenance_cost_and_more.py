# Generated by Django 5.2.1 on 2025-06-09 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='hourly_rate',
        ),
        migrations.RemoveField(
            model_name='roommaintenance',
            name='cost',
        ),
        migrations.AddField(
            model_name='room',
            name='cover_image',
            field=models.ImageField(blank=True, help_text='Upload room cover image', null=True, upload_to='room_covers/'),
        ),
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True, help_text='Room description and additional details'),
        ),
    ]
