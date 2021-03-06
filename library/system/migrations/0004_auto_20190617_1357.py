# Generated by Django 2.2.2 on 2019-06-17 13:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20190617_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_borrowed_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='date returned'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 17, 13, 57, 15, 430842, tzinfo=utc), verbose_name='date published'),
        ),
    ]
