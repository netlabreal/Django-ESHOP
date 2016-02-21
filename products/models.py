#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.conf import settings
from django.core.urlresolvers import reverse


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    img = models.ImageField(upload_to='categorys/', null=True, blank=True)

    class Meta:
        verbose_name_plural = u'Категория'

    def __unicode__(self):
        return self.title

    def get_category_url(self):
        return str(reverse('catalogs', args=[self.slug]))

    def save(self):
        if not self.id:
            self.slug = slugify(timezone.now()).replace('-', '').replace('0', 'f')
        # ext = self.img.filename.split('.')[1]
        super(Category, self).save()

    def delete(self):
        if os.path.exists(self.img.path):
            os.remove(self.img.path)
        super(Category, self).delete()

    def count_products(self):
        products = Products.objects.filter(category=self)
        return products.count()



def image_upload_to(instance, filename):
    slug = slugify(timezone.now()).replace('-', '').replace('0', 'f')
    f_ext = filename.split('.')[1]
    return 'products/%s.%s'%(slug, f_ext)


class Products(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    h = models.CharField(max_length=300, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    category = models.ForeignKey(Category, null=True, blank=True)
    img = models.ImageField(upload_to = image_upload_to, null=True, blank=True)

    class Meta:
        verbose_name_plural = u'Продукты'

    def __unicode__(self):
        return self.title +' - '+str(self.price)


    def get_product_url(self):
        return str(reverse('products', args=[self.pk]))

    def add_to_shopcart(self):
        return ('cartt')
        #return "%s?item=%skol=1" % (reverse('cartt'), str(self.id)+'&')
        #return "%s" % (reverse('cartt'))

    def del_from_shopcart(self):
        return "%s?item=%s&delete=True" % (reverse('cartt'), self.id)
