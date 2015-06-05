from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.mainapp_index, name='mainapp_index'),
    url(r'^league/', views.mainapp_league, name='mainapp_league'),
    url(r'^team/', views.mainapp_team, name='mainapp_team'),
    url(r'^player/', views.mainapp_player, name='mainapp_player'),
    url(r'^match/', views.mainapp_match, name='mainapp_match'),
]
