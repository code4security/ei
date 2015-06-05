"""
batch insert data into db.
the data is obtained from dota2 api site and temporarily stored in json format.
the db is generated according to models.py file.
"""

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ei.settings'
from mainapp.models import League
from mainapp.models import Team
from mainapp.models import Player
import json


def ei_player():
    playerpool_file = open("playerpool.json", "r")
    playerpool_str = playerpool_file.read()
    playerpool = json.loads(playerpool_str)
    queryestlist = []
    for p in playerpool:
        # print(p)
        queryestlist.append(Player(playerid_32=int(p), playerid_64=int(
            playerpool[p]["steamid"]), Player_name=playerpool[p]["personaname"]))
    Player.objects.bulk_create(queryestlist)


def ei_team():
    teaminfo_file = open("teaminfo_original.json", "r")
    teaminfo_str = teaminfo_file.read()
    teaminfo = json.loads(teaminfo_str)
    teams = teaminfo["result"]["teams"]
    queryestlist = []
    for t in teams:
        # print(p)
        queryestlist.append(
            Team(team_id=t["team_id"], team_name=t["name"], team_tag=t["tag"], country_code=t["country_code"]))
    Team.objects.bulk_create(queryestlist)


def ei_league():
    leaguepool_file = open("leaguepool.json", "r")
    leaguepool_str = leaguepool_file.read()
    leaguepool = json.loads(leaguepool_str)
    queryestlist = []
    for l in leaguepool:
        # print(p)
        queryestlist.append(
            League(leagueid=l["leagueid"], league_name=l["name"].strip("#DOTA_Item_")))
    League.objects.bulk_create(queryestlist)

# ei_league()
# ei_team()
# ei_player()
