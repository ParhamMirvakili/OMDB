from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Watchlist
from .serializers import MovieSerializer


@api_view(['GET'])
def get_all_movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def add_movie_to_watchlist(request):
    if request.method == 'POST':
        movies = Movie.objects.all()
        movie_id = request.data.get('movie_id')
        print(movie_id)
        try:
            movie = get_object_or_404(movies, id=movie_id)
            print(movie.name)
        except movie.DoesNotExist:
            return Response({"message": "Movie does not exist"}, status=status.HTTP_404_NOT_FOUND)
        watchlist, created = Watchlist.objects.get_or_create(user=request.user.id)
        if movie in watchlist.movies:
            return Response({"message": "Movie already exists in watchlist"}, status=status.HTTP_400_BAD_REQUEST)
        watchlist.movies.add(movie)
        return Response({"message": f"Movie '{movie.name}' added to watchlist"}, status=status.HTTP_201_CREATED)
