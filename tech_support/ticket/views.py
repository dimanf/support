# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from datetime import datetime, timedelta

from tech_support.ticket.models import Ticket, Comments
from tech_support.department.models import Department
from tech_support.ticket.forms import CreateTicketForm, TicketCommentForm, TikcetFilterForm

class TicketListView(ListView):
	models = Ticket
	queryset = queryset=Ticket.objects.order_by('-date_create')

def TicketDetailView(request, ticket_id):
	ticket = Ticket.objects.get(id=ticket_id)
	if request.method == 'POST':
		form = TicketCommentForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			ticket_comment = Comments(
				text = cd['text'],
				ticket_id = ticket.id)
			ticket_comment.save()
			return HttpResponseRedirect('/')
	else:
		form = TicketCommentForm()

	return render(request, 'ticket/ticket_detail.html', {
		'comment_form': form,
		'ticket': ticket,
		})

def create_ticket(request):
	if request.method == 'POST':
		form = CreateTicketForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data

			ticket = Ticket(
				issue_created_by_user=request.user,
				issue_descr=cd['issue_descr'],
				)

			ticket.save()

			dept_list = Department.objects.filter(id__in=request.POST.getlist('dept'))
			for dept in dept_list:
				ticket.dept.add(dept)

			oper_list = User.objects.filter(id__in=request.POST.getlist('issue_operator'))
			for oper in oper_list:
				ticket.issue_operator.add(oper)

			return HttpResponseRedirect('/')
	else:
		form = CreateTicketForm()

	return render(request, 'ticket/create_ticket.html', {
		'ticket_form': form,
		})

def change_ticket(request, ticket_id):
	ticket = Ticket.objects.get(id=ticket_id)
	dept_list = Department.objects.all()
	users_list = User.objects.all()

	if request.method == 'POST':
		form = CreateTicketForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			ticket.issue_descr = cd['issue_descr']

			dept_list = dept_list.filter(id__in=request.POST.getlist('dept'))
			ticket.dept.clear()
			for dept in dept_list:
				ticket.dept.add(dept)

			oper_list = users_list.filter(id__in=request.POST.getlist('issue_operator'))
			ticket.issue_operator.clear()
			for oper in oper_list:
				ticket.issue_operator.add(oper)
			ticket.save()
			return HttpResponseRedirect('/%s/' % ticket_id)
	else:
		form = CreateTicketForm(initial={
			'issue_descr': ticket.issue_descr,
			})

	return render(request, 'ticket/change_ticket.html', {
		'change_form': form,
		'users_list': users_list,
		'dept_list': dept_list,
		'ticket': ticket,
		})

def statistic(request):
	ticket_filtred = Ticket.objects.all()

	filter_value = request.GET.get('filer_value', '')

	if filter_value == 'yesterday':
		yesterday = datetime.now()-timedelta(1)
		ticket_filtred = ticket_filtred.filter(date_create__range=(yesterday, datetime.now()))

	if filter_value == 'last_week':
		last_week = datetime.now()-timedelta(7)
		ticket_filtred = ticket_filtred.filter(date_create__range=(last_week, datetime.now()))

	if filter_value == 'last_month':
		last_month = datetime.now()-timedelta(30)
		ticket_filtred = ticket_filtred.filter(date_create__range=(last_month, datetime.now()))

	ticket_not_accept = ticket_filtred.filter(status='not_accept').count()
	ticket_in_process = ticket_filtred.filter(status='in_process').count()
	ticket_end_process = ticket_filtred.filter(status='end_process').count()

	form = TikcetFilterForm()

	return render(request, 'ticket/statistic_ticket.html', {
		'ticket_not_accept': ticket_not_accept,
		'ticket_in_process': ticket_in_process,
		'ticket_end_process': ticket_end_process,
		'form': form,
		'ticket_filtred': ticket_filtred,
		})