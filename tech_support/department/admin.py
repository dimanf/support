# -*- coding: utf-8 -*-
from django.contrib import admin
from tech_support.department.models import Department

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'date_create',)
	list_display_links = ('name', )
	search_fields = ('name', )

admin.site.register(Department, DepartmentAdmin)