# Generated by Django 5.1.1 on 2024-11-16 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_remove_appointment_email_remove_appointment_patient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient_name',
            field=models.CharField(default='Introduce your name', max_length=100),
        ),
    ]
