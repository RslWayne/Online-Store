# Generated by Django 3.1.5 on 2021-02-10 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210207_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(default=datetime.date(2021, 2, 10)),
        ),
    ]
