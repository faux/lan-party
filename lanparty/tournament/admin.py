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

class TeamAdmin(admin.ModelAdmin):
    inlines = (TeamMembershipInline,)
    form = TeamForm

class TournamentAdmin(admin.ModelAdmin):
    inlines = (TournamentServerInline,TournamentTeamInline)
    form = TournamentForm


