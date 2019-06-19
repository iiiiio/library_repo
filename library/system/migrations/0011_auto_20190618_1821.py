# Generated by Django 2.2.2 on 2019-06-18 10:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_auto_20190618_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fine',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 18, 10, 21, 45, 633268, tzinfo=utc), verbose_name='date published'),
        ),
    ]
