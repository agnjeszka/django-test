# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zamowienie',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('l1', models.FloatField()),
                ('l2', models.FloatField()),
                ('l3', models.FloatField()),
                ('l4', models.FloatField()),
                ('l5', models.FloatField()),
                ('l6', models.FloatField()),
                ('listwa1', models.BooleanField()),
                ('listwa2', models.BooleanField()),
                ('listwa3', models.BooleanField()),
                ('listwa4', models.BooleanField()),
                ('listwa5', models.BooleanField()),
                ('listwa6', models.BooleanField()),
                ('listwa7', models.BooleanField()),
                ('listwa8', models.BooleanField()),
            ],
        ),
    ]
