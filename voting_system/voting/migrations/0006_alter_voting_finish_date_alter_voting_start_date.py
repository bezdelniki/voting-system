# Generated by Django 5.0.1 on 2024-01-31 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_remove_votingprocess_is_secret_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='finish_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 31, 18, 54, 48, 486029)),
        ),
        migrations.AlterField(
            model_name='voting',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 31, 18, 54, 48, 486029)),
        ),
    ]
