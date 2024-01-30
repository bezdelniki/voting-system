# Generated by Django 5.0.1 on 2024-01-30 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='is_secret',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='votingprocess',
            name='is_secret',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='voting',
            name='finish_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 31, 2, 52, 54, 370439)),
        ),
        migrations.AlterField(
            model_name='voting',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 31, 2, 52, 54, 370439)),
        ),
    ]