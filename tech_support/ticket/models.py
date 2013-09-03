# -*- coding: utf-8 -*-
import random
import string

from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from tech_support.department.models import Department

class Ticket(models.Model):
	SOLVED_CHOICE = (
			('not_accept', u'Не приянта'),
			('in_process', u'В процессе'),
			('end_process', u'Завершена')
		)

	issue_created_by_user = models.ForeignKey(User, related_name='u+', verbose_name=u'Завка от пользователя')
	issue_operator = models.ManyToManyField(User, related_name='ref+', verbose_name=u'Заявку принял(и)')
	nomber_of_issue = models.CharField(u'Номер заявки', max_length=30, null=True, blank=True, unique=True)
	date_create = models.DateTimeField('Дата создания', auto_now_add=True)
	date_update = models.DateTimeField('Дата обновления', auto_now=True)
	issue_descr = models.TextField(u'Текст')
	dept = models.ManyToManyField(Department, verbose_name=u'Отдел')
	status = models.CharField(u'Статус тикета', choices=SOLVED_CHOICE, max_length=30, default='not_accept')
	history = HistoricalRecords()

	def save(self, *args, **kwargs):
		if not self.nomber_of_issue:
			self.nomber_of_issue = ''.join(random.choice(string.digits) for i in range(8))
			super(Ticket, self).save()
		super(Ticket, self).save()

	def get_status(self):
		status = ''
		if self.status == 'not_accept':
			status = u'Не приянта'
		elif self.status == 'in_process':
			status = u'В процессе'
		elif self.status == 'end_process':
			status = u'Завершена'
		return status

	def get_comments(self):
		return self.comments_set.all()

	def __unicode__(self):
		return u'Заявка № %s' % self.nomber_of_issue

	class Meta:
		verbose_name = u'Тикет'
		verbose_name_plural = u'Тикет'

class Comments(models.Model):
	text = models.TextField(u'Текст комментария')
	date_create = models.DateTimeField(u'Дата создания', auto_now=True)
	ticket = models.ForeignKey(Ticket, verbose_name=u'Тикет')

	def __unicode__(self):
		return u'Комментарий к тикету - %s' % self.ticket

	class Meta:
		verbose_name = u'Комментарий к тикету'
		verbose_name_plural = u'Комментарии к тикетам'