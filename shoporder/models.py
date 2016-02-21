#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from shopcart.models import Cart

class Order(models.Model):
	name = models.CharField(max_length=100)
	email =  models.EmailField()
	cart = models.ForeignKey(Cart)

	def __unicode__(self):
		return self.name+"   "+str(self.cart.itog)

	class Meta:
		verbose_name_plural = 'Заказ'	