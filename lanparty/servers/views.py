from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from models import *

def edit_server(request, id=None):
    if request.method == "POST":
        if id is not None:
            server = get_object_or_404(Server, pk=id)
            if 'delete' in request.POST:
                server.delete()
                return HttpResponseRedirect(reverse('server-list'))
                
            form = ServerForm(request.POST, instance=server)
        else:
            form = ServerForm(request.POST)
        if form.is_valid():
            server = form.save()
            return HttpResponseRedirect(reverse('server-list'))
    else:
        if id is not None:
            server = get_object_or_404(Server, pk=id)
            form = ServerForm(instance=server)
        else:
            form = ServerForm()

    return render_to_response('servers/edit_server.html', {
        'form': form,
    })


def server_list(request):
    servers = Server.objects.all()
    return render_to_response('servers/all.html', {
        'servers': servers,
    })
