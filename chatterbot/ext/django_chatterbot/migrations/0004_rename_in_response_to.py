# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 23:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_chatterbot', '0003_change_occurrence_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='statement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_response', to='django_chatterbot.Statement'),
        ),
        migrations.AlterField(
            model_name='response',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='django_chatterbot.Statement'),
        ),
    ]
