# Generated by Django 5.1.1 on 2024-10-12 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='ID',
            new_name='sensor',
        ),
    ]
