# Generated by Django 5.1.1 on 2024-11-16 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0012_alter_appointment_requested_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='requested_appointment_date',
            field=models.CharField(max_length=19),
        ),
    ]
