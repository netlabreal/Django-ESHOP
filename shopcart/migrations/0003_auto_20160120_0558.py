# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20160119_0421'),
        ('shopcart', '0002_auto_20160120_0549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ManyToManyField(to='products.Products', through='shopcart.Citem'),
        ),
        migrations.AddField(
            model_name='citem',
            name='cart',
            field=models.ForeignKey(blank=True, to='shopcart.Cart', null=True),
        ),
    ]
