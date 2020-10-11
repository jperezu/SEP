from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/event', views.event_request, name='event_form'),
    path('eventreq', views.get_pending_events, name='eventreq_list'),
    path('eventreq/csaccept', views.pending_event_cs_accept, name='event_cs_accept'),
    path('eventreq/reject', views.pending_event_reject, name='event_reject'),
    path('eventreqbud', views.get_cs_accepted_events, name='eventcs_list'),
    path('eventreq/financialaccept', views.pending_event_financial_accept, name='event_financial_accept'),
    path('eventreqfin', views.get_fin_accepted_events, name='eventfin_list'),
    path('eventreq/adminaccept', views.pending_event_admin_accept, name='event_admin_accept'),
    path('create/event', views.create_event, name='create_event'),
    path('remove/event', views.remove_req_event, name='remove_request'),
    path('events', views.show_events, name='events_progress'),
    path('tasks/assign', views.assign_tasks, name='start_event'),
    path('task/remove', views.remove_task, name='remove_task'),
    path('task', views.get_tasks, name='get_tasks'),
    path('task/status', views.set_task_status, name='set_task_status'),
    path('event/archive', views.archive_event, name='archive_event'),
    path('login', views.login_view, name='login'),

]