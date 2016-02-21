# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20160111_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(blank=True, to='products.Category', null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(null=True, upload_to=b'categorys/', blank=True),
        ),
    ]
