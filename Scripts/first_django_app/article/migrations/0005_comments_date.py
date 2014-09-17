# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_comments_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 12, 15, 35, 36, 40000)),
            preserve_default=True,
        ),
    ]
