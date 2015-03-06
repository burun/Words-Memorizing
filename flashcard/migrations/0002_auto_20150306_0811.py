# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flashcard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlashCard',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('front', models.TextField(max_length=255, verbose_name='Front')),
                ('back', models.TextField(max_length=255, verbose_name='Back')),
                ('next_practice', models.DateField(auto_now_add=True)),
                ('times_practiced', models.PositiveIntegerField(default=1)),
                ('easy_factor', models.FloatField(default=2.5)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Flashcards',
                'verbose_name': 'Flashcard',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='card',
            name='back',
        ),
        migrations.RemoveField(
            model_name='card',
            name='front',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='cards',
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='left',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='right',
        ),
        migrations.DeleteModel(
            name='Deck',
        ),
        migrations.RemoveField(
            model_name='word',
            name='siblings',
        ),
        migrations.RemoveField(
            model_name='word',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='Word',
        ),
    ]
