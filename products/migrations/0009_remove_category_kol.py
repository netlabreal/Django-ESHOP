# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20160112_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='kol',
        ),
    ]
