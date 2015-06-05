# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('playerid_32', models.IntegerField()),
                ('playerid_64', models.IntegerField()),
                ('Player_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('team_id', models.IntegerField()),
                ('team_name', models.CharField(max_length=50)),
                ('team_tag', models.CharField(max_length=50)),
                ('country_code', models.IntegerField()),
                ('player1', models.CharField(max_length=50)),
                ('player2', models.CharField(max_length=50)),
                ('player3', models.CharField(max_length=50)),
                ('player4', models.CharField(max_length=50)),
                ('player5', models.CharField(max_length=50)),
            ],
        ),
    ]
