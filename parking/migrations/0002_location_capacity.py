# Generated by Django 5.0.7 on 2024-07-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='capacity',
            field=models.IntegerField(default=50),
        ),
    ]