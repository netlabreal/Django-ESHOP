# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to=b'/categorys/')),
            ],
            options={
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
            },
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b'},
        ),
    ]
