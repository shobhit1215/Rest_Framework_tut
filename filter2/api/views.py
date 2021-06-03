from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class StudentList(ListAPIView):
    #This will filter the records on the basis of various fields
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #We will write studentapi/?city=city_name in the URL
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','city']

