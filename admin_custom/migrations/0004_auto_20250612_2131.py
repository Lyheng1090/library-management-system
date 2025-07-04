# Generated by Django 5.2.1 on 2025-06-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_custom', '0003_add_staff_personal_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='age',
            field=models.PositiveIntegerField(default=25),
        ),
        migrations.AddField(
            model_name='staff',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1),
        ),
    ]
