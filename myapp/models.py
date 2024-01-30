from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.name


class Watchlist(models.Model):
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE,  null=True, blank=True)

