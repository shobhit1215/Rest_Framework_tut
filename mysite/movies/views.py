from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer

# Creating endpoints for action movies
class ActionMovie(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre='Action')
    serializer_class = MovieSerializer

