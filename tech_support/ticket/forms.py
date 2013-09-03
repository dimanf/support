# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from tech_support.department.models import Department

class CreateTicketForm(forms.Form):
	TICKET_CHOICE = [(name.id, name.name) for name in Department.objects.all()]
	PERSONAL_UESERS = [(user.id, user.username) for user in User.objects.all()]

	issue_descr = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Введите текст'}), label=u'Текст тикета')
	dept = forms.MultipleChoiceField(choices=TICKET_CHOICE, widget=forms.CheckboxSelectMultiple(), required=False, label=u'Отделы')
	issue_operator = forms.MultipleChoiceField(choices=PERSONAL_UESERS, widget=forms.CheckboxSelectMultiple(), required=False, label=u'Назначить ответственных')

class TicketCommentForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Введите текст'}), label=u'Текст комментария')

class TikcetFilterForm(forms.Form):
	FILTER_CHOICE = (
			('yesterday', u'За вчерашний день'),
			('last_week', u'За последнюю неделю'),
			('last_month', u'За последний месяц')
		)

	filer_value = forms.ChoiceField(FILTER_CHOICE, widget=forms.RadioSelect(), label=u'Период')