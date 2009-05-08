from django.contrib import admin
from models import *

class TournamentServerInline(admin.TabularInline):
    model = TournamentServer
    extra = 10

class TeamMembershipInline(admin.TabularInline):
    model = TeamMembership
    extra = 5

class TournamentTeamInline(admin.TabularInline):
    model = Team
    extra = 5

class MatchInline(admin.TabularInline):
    model = Match
    extra = 5

class TeamMatchInline(admin.TabularInline):
    model = TeamMatch
    extra = 5

class TeamAdmin(admin.ModelAdmin):
    inlines = (TeamMembershipInline,)
    form = TeamForm

class TournamentAdmin(admin.ModelAdmin):
    inlines = (TournamentServerInline,TournamentTeamInline)
    form = TournamentForm

class RoundAdmin(admin.ModelAdmin):
    inlines = (MatchInline,)

class MatchAdmin(admin.ModelAdmin):
    inlines = (TeamMatchInline,)

