# Generated by Django 5.0 on 2024-01-05 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_sms_count'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sms_count',
            new_name='smscount',
        ),
    ]
