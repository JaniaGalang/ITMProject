# Generated by Django 5.0.7 on 2024-07-20 02:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0011_remove_reservation_date_reserved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='date_reserved',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
