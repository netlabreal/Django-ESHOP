# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_products_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='h',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
