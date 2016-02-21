#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from products.models import Products
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save, post_save, post_delete
from decimal import Decimal


class Citem(models.Model):
    cart = models.ForeignKey("Cart", null=True, blank=True)
    item = models.ForeignKey(Products)
    kol = models.PositiveIntegerField(default=1)
    total = models.DecimalField(decimal_places=2, max_digits=20, default=0)

    class Meta:
        verbose_name_plural = u'Элементы корзины'


    def __unicode__(self):
        return self.item.title


def before_save_Citem(sender, instance, *args, **kwargs):
    kol = instance.kol
    cena = instance.item.price
    instance.total = Decimal(kol)*Decimal(cena)


def after_save_Citem(sender, instance, *args, **kwargs):
    instance.cart.update_itog()


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    item = models.ManyToManyField(Products, through=Citem)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    itog = models.DecimalField(decimal_places=2, max_digits=20, default=0)

    def update_itog(self):
        itog = 0
        for item in self.citem_set.all():
        	itog += item.total
        self.itog = itog
        self.save()

    def kol_items(self):
        return Citem.objects.filter(cart=self).count()

    class Meta:
        verbose_name_plural = 'Корзина'    

pre_save.connect(before_save_Citem, sender=Citem)
post_save.connect(after_save_Citem, sender=Citem)
post_delete.connect(after_save_Citem, sender=Citem)