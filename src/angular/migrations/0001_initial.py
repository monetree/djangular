# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-30 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Angular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='default name', max_length=60, null=True)),
                ('number', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
