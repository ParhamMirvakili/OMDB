from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Watchlist
from .serializers import MovieSerializer
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Movie


@api_view(['GET'])
def get_all_movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_to_watchlist(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({"message": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        movie_id = request.data.get('movie_id')
        user = request.user
        if user.watchlist:
            watchlist = user.watchlist
        else:
            watchlist = Watchlist.objects.create()
            user.watchlist = watchlist
            user.save()
        movie = Movie.objects.get(id=movie_id)
        watchlist.movies.append(movie.id)
        watchlist.save()
        return redirect('watchlist')
