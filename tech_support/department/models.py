# -*- coding: utf-8 -*-
from django.db import models

class Department(models.Model):
	name = models.CharField(u'Название отдела', max_length=30)
	date_create = models.DateTimeField(u'Дата создания', auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u'Отдел'
		verbose_name_plural = u'Отделы'