# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2021-03-30 17:25
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('control2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='ask_answer',
            field=otree.db.models.BooleanField(choices=[[True, '예'], [False, 'No']], verbose_name='Your answer:'),
        ),
    ]