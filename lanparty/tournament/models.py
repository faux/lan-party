from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from lanparty.servers.models import Server

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    held_on = models.DateField(blank=True, null=True)
    in_progress = models.BooleanField(default=False)
    servers = models.ManyToManyField(Server, through='TournamentServer')

    def __unicode__(self):
        if self.in_progress:
            return "%s on %s --- In Progress" % (self.name, self.held_on)
        else:
            return "%s on %s" % (self.name, self.held_on)


class TournamentServer(models.Model):
    tournament = models.ForeignKey(Tournament)
    server = models.ForeignKey(Server)
    in_use = models.BooleanField(default=False)

class Team(models.Model):
    name = models.CharField(max_length=100)
    tournaments = models.ManyToManyField(Tournament, null=True, blank=True)
    members = models.ManyToManyField(User, through='TeamMembership')

    def __unicode__(self):
        return "Team '%s'" % self.name

class TeamMembership(models.Model):
    team = models.ForeignKey(Team)
    user = models.ForeignKey(User)
    leader = models.BooleanField(default=False)

class TournamentServerInline(admin.TabularInline):
    model = TournamentServer
    extra = 10

class TeamMembershipInline(admin.TabularInline):
    model = TeamMembership
    extra = 5

class TeamAdmin(admin.ModelAdmin):
    inlines = (TeamMembershipInline,)

class TournamentAdmin(admin.ModelAdmin):
    inlines = (TournamentServerInline,)

