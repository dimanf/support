# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from tech_support.ticket.views import (
	TicketListView, TicketDetailView, create_ticket,
	change_ticket, statistic)

urlpatterns = patterns('',
	url(r'^$', TicketListView.as_view(), name='ticket'),
	url(r'^(\d+)/$', TicketDetailView, name='ticket_id'),
	url(r'^create_ticket/$', create_ticket),
	url(r'^change_ticket/(\d+)/$', change_ticket),
	url(r'^statistic/$', statistic),
)