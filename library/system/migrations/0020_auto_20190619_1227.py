# Generated by Django 2.2.2 on 2019-06-19 04:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0019_auto_20190619_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='notice_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 19, 4, 27, 40, 746261, tzinfo=utc), verbose_name='date published'),
        ),
    ]
