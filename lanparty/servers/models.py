from django.db import models
from django import forms
from django.contrib import admin
import re

class Server(models.Model):
    name = models.CharField(max_length=100)
    game_type = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=50)
    port = models.IntegerField()
    use_steam = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s --- %s --- %s:%s" % (self.name, self.game_type, self.ip_address, self.port)

class ServerForm(forms.ModelForm):

    def clean_ip_address(self):
        if self.is_valid():
            ip_address = self.cleaned_data['ip_address']
            if not re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip_address):
                if not re.match("^[a-zA-Z][\w.]*$", ip_address):
                    raise forms.ValidationError("Invalid IP address or host name")
            return ip_address

    def clean_port(self):
        if self.is_valid():
            port = self.cleaned_data['port']
            if port < 0 or port > 65535:
                raise forms.ValidationError("Invalid port")
            return port
            


    class Meta:
        model = Server

class ServerAdmin(admin.ModelAdmin):
    form = ServerForm


