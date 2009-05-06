from django.conf.urls.defaults import *
from django.contrib import admin
from lanparty.servers.models import *
from lanparty.tournament.models import *

admin.autodiscover()

admin.site.register(Server, ServerAdmin)
admin.site.register(Tournament, TournamentAdmin)

urlpatterns = patterns('',
    # Example:
    # (r'^lanparty/', include('lanparty.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    url(r'^users/', include('lanparty.users.urls')),
    url(r'^servers/', include('lanparty.servers.urls')),
    url(r'^tournament/', include('lanparty.tournament.urls')),
)
