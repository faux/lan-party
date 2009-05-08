from django.contrib import admin
from models import *

class ServerAdmin(admin.ModelAdmin):
    form = ServerForm


