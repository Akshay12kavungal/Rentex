# Generated by Django 5.0.7 on 2024-07-26 07:17

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('profilemanagement', '0007_alter_order_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='item_name',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2024, 7, 27, 7, 17, 36, 484044, tzinfo=datetime.timezone.utc)),
        ),
    ]
