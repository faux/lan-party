from django.db import models
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from lanparty.servers.models import Server

PAYMENT_CHOICES = (
    ('T', 'Team'),
    ('P', 'Player'),
)

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    held_on = models.DateField(blank=True, null=True)
    in_progress = models.BooleanField(default=False)
    servers = models.ManyToManyField(Server, through='TournamentServer')
    cost = models.IntegerField(blank=True, null=True)
    payment_type = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default='P')

    def __unicode__(self):
        if self.in_progress:
            return "%s on %s --- In Progress" % (self.name, self.held_on)
        else:
            return "%s on %s" % (self.name, self.held_on)

    def teams_paid(self):
        return [t.is_paid() for t in self.team_set.all()]

    def get_teams_paid_display(self):
        teams_paid = self.teams_paid()
        if all(teams_paid):
            message = "All"
        elif any(teams_paid):
            total = len([p for p in teams_paid if p])
            count = len(teams_paid)
            message = "Some (%s of %s)" % (total, count)
        else:
            message = "None"
        return message + " have paid"
    

class TournamentServer(models.Model):
    tournament = models.ForeignKey(Tournament)
    server = models.ForeignKey(Server)
    in_use = models.BooleanField(default=False)

class Team(models.Model):
    name = models.CharField(max_length=100)
    tournament = models.ForeignKey(Tournament)
    members = models.ManyToManyField(User, through='TeamMembership')

    def __unicode__(self):
        return "Team '%s'" % self.name

    def is_paid(self):
        return all([m.paid for m in self.teammembership_set.all()])

class TeamMembership(models.Model):
    team = models.ForeignKey(Team)
    user = models.ForeignKey(User)
    captain = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        super(TeamMembership, self).save(*args, **kwargs)
        self.team.save()

class TournamentForm(forms.ModelForm):
    teams_paid = forms.CharField(required=False, widget=forms.TextInput(attrs={'disabled': 'disabled'}))

    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs:
            if 'initial' not in kwargs:
                kwargs['initial'] = {}
            kwargs['initial']['teams_paid'] = kwargs['instance'].get_teams_paid_display()
        return super(TournamentForm, self).__init__(*args, **kwargs)
           
    class Meta:
        model = Tournament

class TeamForm(forms.ModelForm):
    paid = forms.CharField(required=False, widget=forms.TextInput(attrs={'disabled': 'disabled'}))

    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs:
            if 'initial' not in kwargs:
                kwargs['initial'] = {}
            kwargs['initial']['paid'] = kwargs['instance'].is_paid()
        return super(TeamForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Team

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

