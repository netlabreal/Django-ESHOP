# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0005_citem_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='itog',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=2),
        ),
    ]
