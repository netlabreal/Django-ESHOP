# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_category_kol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='h',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
