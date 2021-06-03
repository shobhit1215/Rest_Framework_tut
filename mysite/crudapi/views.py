from django.shortcuts import render
#to convert JSON to python
import io
from rest_framework.parsers import JSONParser
#Model
from .models import Student
# Sequilizer Class
from .serializers import StudentSerializer
#To convert python to JSON
from rest_framework.renderers import JSONRenderer
#To send response
from django.http import HttpResponse,JsonResponse
#to exempt Csrf token
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == "GET":
        #Get data from request
        json_data = request.body
        #Convert to python
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        #Get the ID
        id = python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many = True)

        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method =="POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data= python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
        
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        #for compelete update we send entire data and remove partial field from here
        serializer = StudentSerializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Updated data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'Item deleted'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(res,safe=false)

# To convert in class views
# from django.views import View
# class StudentAPI(View):
# def get(self,request,*args,**kwargs):
     # Put the entire above code
# def post(self,request,*args,**kwargs):
#def put(self,request,*args,**kwargs):
#def delete(self,request,*args,**kwargs):






