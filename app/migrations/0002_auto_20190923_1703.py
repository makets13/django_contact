# Generated by Django 2.2.5 on 2019-09-23 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50),
        ),
    ]
