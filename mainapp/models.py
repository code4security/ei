from django.db import models

# Create your models here.


class Team(models.Model):

    """docstring for Team"""
    team_id = models.IntegerField(default=0)
    team_name = models.CharField(max_length=50)
    team_tag = models.CharField(max_length=50)
    country_code = models.CharField(max_length=50)
    player1 = models.CharField(max_length=50)
    player2 = models.CharField(max_length=50)
    player3 = models.CharField(max_length=50)
    player4 = models.CharField(max_length=50)
    player5 = models.CharField(max_length=50)

    def __str__(self):
        return self.team_name


class Player(models.Model):

    """docstring for Player"""
    playerid_32 = models.IntegerField(default=0)
    playerid_64 = models.IntegerField(default=0)
    Player_name = models.CharField(max_length=50)

    def __str__(self):
        return self.Player_name


class League(models.Model):

    """docstring for League"""
    playerid_32 = models.IntegerField(default=0)
    playerid_64 = models.IntegerField(default=0)
    Player_name = models.CharField(max_length=50)

    def __str__(self):
        return self.Player_name
