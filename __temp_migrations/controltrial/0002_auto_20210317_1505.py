# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2021-03-17 20:05
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('controltrial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='question_1',
            field=otree.db.models.IntegerField(null=True, verbose_name='귀하가 첫 번째 사람이고 B를 선택했다고 가정할 때, 두 번째 사람도 B를 선택하면 귀하는 몇 점을 획득하게 됩니까?'),
        ),
    ]