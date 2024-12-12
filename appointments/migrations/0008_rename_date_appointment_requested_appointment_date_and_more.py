# Generated by Django 5.1.1 on 2024-11-16 16:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0007_appointment_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='date',
            new_name='requested_appointment_date',
        ),
        migrations.AddField(
            model_name='appointment',
            name='date_requested',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
