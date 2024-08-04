from django.shortcuts import render
from movie_app.models import Movie, Director, Review
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movie_app.serializers import DirectorSerializer,ReviewSerializer,MovieSerializer


@api_view(['GET'])
def movie_api_view(request):
    movie_first = Movie.objects.all()
    movie_second = MovieSerializer(instance=movie_first,many=True).data
    return Response(data=movie_second)

@api_view(['GET'])
def director_api_view(request):
    director_first = Director.objects.all()
    director_second = DirectorSerializer(instance=director_first).data
    return Response(data=director_second)



@api_view(['GET'])
def review_api_view(request):
    review_first = Director.objects.all()
    review_second = DirectorSerializer(instance=review_first).data
    return Response(data=review_second)


