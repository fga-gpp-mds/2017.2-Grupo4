# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_rating', '0003_auto_20171128_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicalstate_10ymore',
            name='classifier_id',
            field=models.CharField(blank=True, max_length=150, verbose_name='ID do Classificador'),
        ),
        migrations.AddField(
            model_name='clinicalstate_28d',
            name='classifier_id',
            field=models.CharField(blank=True, max_length=150, verbose_name='ID do Classificador'),
        ),
        migrations.AddField(
            model_name='clinicalstate_29d_2m',
            name='classifier_id',
            field=models.CharField(blank=True, max_length=150, verbose_name='ID do Classificador'),
        ),
        migrations.AddField(
            model_name='clinicalstate_2m_3y',
            name='classifier_id',
            field=models.CharField(blank=True, max_length=150, verbose_name='ID do Classificador'),
        ),
        migrations.AddField(
            model_name='clinicalstate_3y_10y',
            name='classifier_id',
            field=models.CharField(blank=True, max_length=150, verbose_name='ID do Classificador'),
        ),
    ]
