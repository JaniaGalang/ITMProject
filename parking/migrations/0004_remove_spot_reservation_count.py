# Generated by Django 5.0.7 on 2024-07-18 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_spot_reservation_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='reservation_count',
        ),
    ]