from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
urlpatterns = patterns('lanparty.users.views',
    # Example:
    # (r'^lanparty/', include('lanparty.foo.urls')),
    url(r'^signin/', 'signin'),
    url(r'^signup/', 'signup', name="signup"),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
