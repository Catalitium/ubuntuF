# Generated by Django 5.1.1 on 2024-11-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_rename_appointment_date_appointment_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(default=1234, max_length=254),
            preserve_default=False,
        ),
    ]
