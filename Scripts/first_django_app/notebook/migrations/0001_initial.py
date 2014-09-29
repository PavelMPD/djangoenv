# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotebookRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('position', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'notebook_rows',
            },
            bases=(models.Model,),
        ),
    ]
