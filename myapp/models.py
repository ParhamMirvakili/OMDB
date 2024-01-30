from django.contrib.postgres.fields import ArrayField
from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.name


class Watchlist(models.Model):
    movies = ArrayField(models.IntegerField(), blank=True, null=True)
