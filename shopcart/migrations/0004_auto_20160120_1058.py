# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0003_auto_20160120_0558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citem',
            old_name='count',
            new_name='kol',
        ),
    ]
