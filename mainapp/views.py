from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader


def mainapp_league(request):
    template = loader.get_template('league.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))


def mainapp_team(request):
    template = loader.get_template('team.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))


def mainapp_player(request):
    template = loader.get_template('player.html')
    context = RequestContext(request, {
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
