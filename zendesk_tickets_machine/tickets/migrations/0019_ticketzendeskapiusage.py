# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 02:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20170103_1313'),
        ('agents', '0001_initial'),
        ('tickets', '0018_remove_ticket_requester_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketZendeskAPIUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(max_length=50)),
                ('priority', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agents.Agent')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Board')),
            ],
        ),
    ]
