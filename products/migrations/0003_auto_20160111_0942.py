# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20160111_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(upload_to=b'categorys/'),
        ),
    ]
