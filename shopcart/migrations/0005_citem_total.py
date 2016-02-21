# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0004_auto_20160120_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='citem',
            name='total',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=2),
        ),
    ]
