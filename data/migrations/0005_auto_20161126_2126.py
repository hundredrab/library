# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-26 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_book_subcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='subcode',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='data.Subject'),
        ),
    ]