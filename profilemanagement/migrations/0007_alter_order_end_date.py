# Generated by Django 5.0.7 on 2024-07-26 06:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilemanagement', '0006_alter_order_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2024, 7, 27, 6, 51, 44, 407953, tzinfo=datetime.timezone.utc)),
        ),
    ]
