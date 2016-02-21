# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20160112_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ImageField(null=True, upload_to=b'products/', blank=True),
        ),
    ]
