from django.shortcuts import render
# wE will create function based views using rest-framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

# @api_view(['GET'])
# def hello(request):
#     return Response({'msg':'Hello World'})

# @api_view(['POST'])
# def hello(request):
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg':'This is POST method','data':request.data})

# @api_view(['GET','POST'])
# def func(request):
#     if request.method == 'GET':
#         return Response({'msg':'Hello World'})
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'This is POST method','data':request.data})

@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if request.method == 'GET':
        #we automaticallt get parsed data not in json
        id = request.data.get('id')
        if id is not None:
           stu = Student.objects.get(id=id)
           serializer = StudentSerializer(stu)
        #    print(serializer.data)
           return Response(serializer.data)
        stu= Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        # print(Response(serializer.data))
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.error)

    if request.method=='DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Deleted !!'})




