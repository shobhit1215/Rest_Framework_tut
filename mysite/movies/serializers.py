from rest_framework import serializers
from .models import Moviedata

#creating serializer class 

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moviedata
        fields = ['id','name','duration','rating','genre']