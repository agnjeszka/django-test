# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalkulatorForm', '0002_typ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zamowienie',
            name='l1',
            field=models.FloatField(blank='True'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='l2',
            field=models.FloatField(blank='True'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='l3',
            field=models.FloatField(blank='True'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='l4',
            field=models.FloatField(blank='True'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='l5',
            field=models.FloatField(blank='True'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='l6',
            field=models.FloatField(blank='True'),
        ),
    ]
