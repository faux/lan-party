from django.conf.urls.defaults import *

urlpatterns = patterns('lanparty.servers.views',
    url(r'^new/', 'edit_server', name='new-server'),
    url(r'^edit/(?P<id>\d+)', 'edit_server', name='edit-server'),
    url(r'^$', 'server_list', name='server-list'),
)
