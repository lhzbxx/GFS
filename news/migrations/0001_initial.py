# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('counter', models.IntegerField(default=0)),
                ('pubDate', models.DateField(auto_now_add=True)),
                ('author', models.CharField(max_length=60)),
            ],
        ),
    ]
