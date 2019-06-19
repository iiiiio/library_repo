# Generated by Django 2.2.2 on 2019-06-18 12:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0011_auto_20190618_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_return_dateline',
            field=models.DateTimeField(default=None, null=True, verbose_name='return dateline'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 18, 12, 0, 1, 654454, tzinfo=utc), verbose_name='date published'),
        ),
    ]
