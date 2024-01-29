from django.urls import path
from .views import add_movie_to_watchlist, get_all_movies

urlpatterns = [
    path('add_movie/', add_movie_to_watchlist, name='add_movie_to_watchlist'),
    path('movies/', get_all_movies, name='get_all_movies'),
]
