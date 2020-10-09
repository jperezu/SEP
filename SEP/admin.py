from django.contrib import admin

from .models import Client, Event, RequestEvent, RequestRecruitment, RequestBudget, Task

admin.site.register(Client)
admin.site.register(Event)

admin.site.register(RequestEvent)
admin.site.register(RequestRecruitment)
admin.site.register(RequestBudget)

admin.site.register(Task)