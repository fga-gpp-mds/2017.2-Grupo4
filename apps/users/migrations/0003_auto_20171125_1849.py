# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-25 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171125_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='comment_receptionist',
            field=models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Comentário do recepcionista'),
        ),
    ]
