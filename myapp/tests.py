# tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Movie, Watchlist


class AddToWatchlistTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.movie = Movie.objects.create(title='Test Movie')
        self.client.login(email='test@example.com', password='password')

    def test_add_to_watchlist(self):
        # Ensure the user initially doesn't have a watchlist
        self.assertFalse(hasattr(self.user, 'watchlist'))

        # Make a POST request to add the movie to the watchlist
        response = self.client.post(reverse('add_to_watchlist', kwargs={'movie_id': self.movie.id}))

        # Check that the response redirects to the watchlist page
        self.assertRedirects(response, reverse('watchlist'))

        # Refresh the user object to get the updated watchlist
        self.user.refresh_from_db()
        # Ensure the user now has a watchlist
        self.assertTrue(hasattr(self.user, 'watchlist'))
        # Check that the movie has been added to the user's watchlist
        self.assertIn(self.movie.id, self.user.watchlist.movies)

    def tearDown(self):
        self.client.logout()
        User.objects.all().delete()
        Movie.objects.all().delete()
