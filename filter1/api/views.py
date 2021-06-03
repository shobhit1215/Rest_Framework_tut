from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student

# Create your views here.

class StudentList(ListAPIView):
    #This will filter the records on the basis of various fields
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #get the students with the value of passby same as that of user
    def get_queryset(self):
        user = self.request.user
        #This will filter the records on the basis of various fields
        return Student.objects.filter(passby=user)

