# Generated by Django 5.1.1 on 2024-11-16 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0009_remove_appointment_date_requested_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(max_length=100),
        ),
    ]
