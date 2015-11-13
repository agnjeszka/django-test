# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalkulatorForm', '0003_auto_20151112_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zamowienie',
            name='l1',
            field=models.FloatField(null='True', blank='True'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='l2',
            field=models.FloatField(null='True', blank='True'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='l3',
            field=models.FloatField(null='True', blank='True'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='l4',
            field=models.FloatField(null='True', blank='True'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='l5',
            field=models.FloatField(null='True', blank='True'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='l6',
            field=models.FloatField(null='True', blank='True'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='listwa1',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='listwa2',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='listwa3',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='listwa4',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='listwa5',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='listwa6',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='listwa7',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='listwa8',
            field=models.NullBooleanField(),
        ),
    ]
