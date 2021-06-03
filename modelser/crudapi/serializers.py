from rest_framework import serializers
from .models import Student
#Model serializer gives us in build validations,inbuild fiels,in build create func


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only = True) with this we cannot update or post name field
    # name = serializers.CharField(validators = [func_name])
    class Meta:
        model = Student
        fields = ['name','roll','city']

    #We apply validations exactly the same way as we applied in validations

   