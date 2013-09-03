# -*- coding: utf-8 -*-
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from tech_support.ticket.models import Ticket, Comments

class TicketAdmin(SimpleHistoryAdmin):
	list_display = ('issue_created_by_user', 'nomber_of_issue', 'date_create', 'date_update', 'status' )
	list_display_links = ('issue_created_by_user', )
	list_filter = ('issue_created_by_user', 'date_create', 'status' )
	search_fields = ('issue_created_by_user', 'nomber_of_issue', 'text', 'date_create', 'status' )
	filter_horizontal = ('dept', 'issue_operator', )
	readonly_fields = ('nomber_of_issue', )

class CommentsAdmin(admin.ModelAdmin):
	list_display = ('ticket', 'text', 'date_create', )
	list_display_links = ('ticket', )
	list_filter = ('ticket', 'text', 'date_create', )
	search_fields = ('ticket', 'text', 'date_create', )

admin.site.register(Comments, CommentsAdmin)
admin.site.register(Ticket, TicketAdmin)
