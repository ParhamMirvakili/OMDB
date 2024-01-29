from django.test import TestCase, Client
from rest_framework import status
from .models import Movie


class AddMovieToWatchlistTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_movie_to_watchlist(self):
        movie = Movie.objects.create(name="Test Movie")
        response = self.client.post('/add_movie/', {'movie_id': movie.id}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], f"Movie '{movie.name}' added to watchlist")
