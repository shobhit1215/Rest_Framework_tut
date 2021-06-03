from rest_framework import serializers

# Create a serializer class to convert  complex objects into python datatype

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=200)