from django.db import models
from django.contrib import admin
from lanparty.servers.models import Server

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    held_on = models.DateField(blank=True, null=True)
    in_progress = models.BooleanField(default=False)
    servers = models.ManyToManyField(Server, through='TournamentServer')

    def __unicode__(self):
        if self.in_progress:
            return "%s --- %s --- In Progress" % (self.name, self.held_on)
        else:
            return "%s --- %s" % (self.name, self.held_on)


class TournamentServer(models.Model):
    tournament = models.ForeignKey(Tournament)
    server = models.ForeignKey(Server)
    in_use = models.BooleanField(default=False)

class TournamentServerInline(admin.TabularInline):
    model = TournamentServer
    extra = 1

class TournamentAdmin(admin.ModelAdmin):
    inlines = (TournamentServerInline,)

