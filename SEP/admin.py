from django.contrib import admin

from .models import Client, Event, RequestEvent

admin.site.register(Client)
admin.site.register(Event)

admin.site.register(RequestEvent)