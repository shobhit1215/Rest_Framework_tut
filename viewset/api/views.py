#Concrete View classes are inherited from GenericAPIView and Mixin Class
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

class StudentViewSet(viewsets.ViewSet):

    def list(self,request):
        print("****************LIST**********")
        print("Basename:",self.basename)
        print("ACtion",self.action)
        print("Detail",self.detail)
        print("Suffix:",self.suffix)
        print("Name",self.name)
        print("Description",self.description)

        stu=Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        print("****************LIST**********")
        print("Basename:",self.basename)
        print("ACtion",self.action)
        print("Detail",self.detail)
        print("Suffix:",self.suffix)
        print("Name",self.name)
        print("Description",self.description)
        id = pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)

    #Similarly define create,update,partial_update,destroy function
