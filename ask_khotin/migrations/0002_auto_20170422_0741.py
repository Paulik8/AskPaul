# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_khotin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question2',
            name='published_date',
            field=models.DateTimeField(null=True, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='question2',
            name='text',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
