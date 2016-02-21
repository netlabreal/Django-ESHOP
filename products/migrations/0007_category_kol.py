# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_products_h'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='kol',
            field=models.IntegerField(default=0),
        ),
    ]
