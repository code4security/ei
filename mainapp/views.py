from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import League
from .models import Team
from .models import Player


def mainapp_league(request):
    league_list = League.objects.order_by('leagueid')
    template = loader.get_template('league.html')
    context = RequestContext(request, {
        'league_list': league_list,
    })
    return HttpResponse(template.render(context))


def mainapp_team(request):
    team_list = Team.objects.order_by('team_id')
    template = loader.get_template('team.html')
    context = RequestContext(request, {
        'team_list': team_list,
    })
    return HttpResponse(template.render(context))


def mainapp_player(request):
    player_list = Player.objects.order_by('playerid_64')
    template = loader.get_template('player.html')
    context = RequestContext(request, {
        'player_list': player_list,
    })
    return HttpResponse(template.render(context))


def mainapp_match(request):
    template = loader.get_template('match.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))


def mainapp_index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))
