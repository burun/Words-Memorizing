# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0002_auto_20150306_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='next_practice',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
