# Generated by Django 5.1.1 on 2024-10-14 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_rename_sensor_id_measurement_sensor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor',
            new_name='senso',
        ),
    ]
