# Generated by Django 4.0.6 on 2022-10-22 09:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date_created',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 10, 22, 4, 25, 51, 833368)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 10, 22, 4, 25, 51, 832861)),
        ),
        migrations.AlterField(
            model_name='revenue',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 22, 4, 25, 51, 833760)),
        ),
    ]
