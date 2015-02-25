# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('cards', models.ManyToManyField(to='flashcard.Card', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('siblings', models.ManyToManyField(to='flashcard.Word', null=True, blank=True, related_name='siblings_rel_+')),
                ('tags', models.ManyToManyField(to='flashcard.Tag', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='deck',
            name='left',
            field=models.ManyToManyField(to='flashcard.Tag', related_name='left_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deck',
            name='right',
            field=models.ManyToManyField(to='flashcard.Tag', null=True, blank=True, related_name='right_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='back',
            field=models.ForeignKey(to='flashcard.Word', related_name='back_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='front',
            field=models.ForeignKey(to='flashcard.Word', related_name='front_set'),
            preserve_default=True,
        ),
    ]
