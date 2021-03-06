# Generated by Django 2.2.2 on 2019-06-18 14:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0016_auto_20190618_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_reservation_end_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='reservation end'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_reserved_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='reserved_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='book_reserved_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='date reserved'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_borrowed_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='borrowed_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 18, 14, 42, 0, 791402, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='BookReservation',
        ),
    ]
