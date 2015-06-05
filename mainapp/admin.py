from django.contrib import admin

# Register your models here.

from .models import League
from .models import Team
from .models import Player

admin.site.register(League)
admin.site.register(Team)
admin.site.register(Player)
