# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leagueid', models.IntegerField(default=0)),
                ('league_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='player',
            old_name='Player_name',
            new_name='player_name',
        ),
        migrations.AlterField(
            model_name='player',
            name='playerid_32',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='playerid_64',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='country_code',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_id',
            field=models.IntegerField(default=0),
        ),
    ]
