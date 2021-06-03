from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse
# Create your views here.

#Model Object

#Function based view to serialize the detail of a particular student
def student_detail(request,pk):
    # get student
    stu = Student.objects.get(id = pk)
    # print(stu)
    #serialize it
    serializer = StudentSerializer(stu)
    # print(serializer)
    # print(serializer.data)
    #convert python data type to json
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    #render it on web page
    return HttpResponse(json_data,content_type='application/json')


def student_list(request):
    # get students
    stu = Student.objects.all()
    # print(stu)
    #serialize it
    serializer = StudentSerializer(stu,many=True)
    # print(serializer)
    # print(serializer.data)
    #convert python data type to json
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    #render it on web page
    return HttpResponse(json_data,content_type='application/json')
