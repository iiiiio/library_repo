# Generated by Django 2.2.2 on 2019-06-19 03:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0017_auto_20190618_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_borrowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='has_reserved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 19, 3, 47, 24, 291915, tzinfo=utc), verbose_name='date published'),
        ),
    ]
