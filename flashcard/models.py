from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Word(models.Model):

    name = models.CharField(max_length=50, unique=True)

    siblings = models.ManyToManyField('self', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    front = models.ForeignKey(Word, related_name="front_set")
    back = models.ForeignKey(Word, related_name="back_set")


class Deck(models.Model):
    name = models.CharField(max_length=50, unique=True)

    left = models.ManyToManyField(Tag, related_name='left_set')
    right = models.ManyToManyField(
        Tag, related_name='right_set', blank=True, null=True)
    cards = models.ManyToManyField(Card, blank=True, null=True)

    def __str__(self):
        return self.name
