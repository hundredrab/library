# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-26 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_remove_book_subcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='subcode',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='data.Subject'),
            preserve_default=False,
        ),
    ]
