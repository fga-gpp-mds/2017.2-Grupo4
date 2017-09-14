# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(help_text='Informe seu nome de usuário', max_length=150, unique=True, verbose_name='Nome de usuário')),
                ('id_user', models.CharField(help_text='Informe seu ID de usuário', max_length=150, unique=True, verbose_name='ID de usuário')),
                ('email', models.EmailField(default='', max_length=254, unique=True, verbose_name='Email do usuário')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('staff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Staff')),
                ('name', models.CharField(help_text='Informe seu nome', max_length=150, verbose_name='Nome')),
                ('uf', models.CharField(max_length=50, verbose_name='UF')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('neighborhood', models.CharField(max_length=100, verbose_name='Neighborhood')),
                ('street', models.CharField(max_length=100, verbose_name='Street')),
                ('block', models.CharField(max_length=50, verbose_name='Block')),
                ('number', models.CharField(max_length=10, verbose_name='Number')),
            ],
            options={
                'abstract': False,
            },
            bases=('users.staff', models.Model),
        ),
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('staff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Staff')),
                ('name', models.CharField(help_text='Informe seu nome', max_length=150, verbose_name='Nome')),
                ('uf', models.CharField(max_length=50, verbose_name='UF')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('neighborhood', models.CharField(max_length=100, verbose_name='Neighborhood')),
                ('street', models.CharField(max_length=100, verbose_name='Street')),
                ('block', models.CharField(max_length=50, verbose_name='Block')),
                ('number', models.CharField(max_length=10, verbose_name='Number')),
            ],
            options={
                'abstract': False,
            },
            bases=('users.staff', models.Model),
        ),
    ]
