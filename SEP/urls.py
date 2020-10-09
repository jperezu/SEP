from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/event', views.event_request, name='event_form'),
    path('list/eventreq', views.get_pending_events, name='eventreq_list'),
    path('list/eventreq/csaccept', views.pending_event_cs_accept, name='event_cs_accept'),
    path('list/eventreq/reject', views.pending_event_reject, name='event_reject'),
    path('list/eventreqbud', views.get_cs_accepted_events, name='eventcs_list'),
    path('list/eventreq/financialaccept', views.pending_event_financial_accept, name='event_financial_accept'),
    path('list/eventreqfin', views.get_fin_accepted_events, name='eventfin_list'),
    path('list/eventreq/adminaccept', views.pending_event_admin_accept, name='event_admin_accept'),
    path('list/create/event', views.create_event, name='create_event'),
    path('list/remove/event', views.remove_req_event, name='remove_request'),
]