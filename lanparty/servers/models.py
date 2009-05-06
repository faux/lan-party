from django.db import models
from django import forms

class Server(models.Model):
    name = models.CharField(max_length=100)
    game_type = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=50)
    port = models.IntegerField()
    use_steam = models.BooleanField(default=False)

    def __unicode__(self):
        return "<Server: %s, %s: %s:%s >" % (self.name, self.game_type, self.ip_address, self.port)



class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
