# Generated by Django 5.0.7 on 2024-07-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0004_remove_spot_reservation_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='is_available',
        ),
        migrations.AddField(
            model_name='spot',
            name='available_slots',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='spot',
            name='total_capacity',
            field=models.IntegerField(default=50),
        ),
    ]