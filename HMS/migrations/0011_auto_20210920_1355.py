# Generated by Django 3.2.6 on 2021-09-20 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0010_auto_20210919_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 13, 55, 53, 642524)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 14, 55, 53, 642524)),
        ),
    ]
