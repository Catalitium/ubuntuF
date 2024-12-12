# Generated by Django 5.1.1 on 2024-11-16 16:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0008_rename_date_appointment_requested_appointment_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='date_requested',
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
