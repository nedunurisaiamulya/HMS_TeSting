# Generated by Django 2.1.3 on 2020-05-24 02:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthNet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateField(default=datetime.date(2020, 5, 23)),
        ),
    ]
