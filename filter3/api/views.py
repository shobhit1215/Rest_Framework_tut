from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

# Create your views here.

class StudentList(ListAPIView):
    #This will filter the records on the basis of various fields
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #Search Filter ***************************
    # We will write studentapi/?search=Mumbai to search a field

    # filter_backends = [SearchFilter]
    # search_fields = ['city']

    #If we give multiple fields then search will take place with any one field
    #search which starts with a particular word
    # search_fields = ['^name']



    #Ordering Filters ************************

    filter_backends = [OrderingFilter]
    ordering_fields = ['name']
    

