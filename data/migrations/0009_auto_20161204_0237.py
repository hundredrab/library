# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-03 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_remove_book_subcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FileField(upload_to=b''),
        ),
    ]
