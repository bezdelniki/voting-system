# Generated by Django 5.0.1 on 2024-01-31 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0009_alter_voting_finish_date_alter_voting_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='finish_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 1, 2, 31, 43, 953478)),
        ),
        migrations.AlterField(
            model_name='voting',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 1, 2, 31, 43, 953478)),
        ),
        migrations.DeleteModel(
            name='SendResults',
        ),
    ]
