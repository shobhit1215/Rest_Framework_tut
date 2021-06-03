from rest_framework import serializers
from .models import Student
#In this we have applied various validations like 100<roll<200

#Validators  =  used for reusability of code

def roll_greater(value):
    if value<100:
        raise serializers.ValidationError('Roll should be geater than 100')
    return value

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField(validators=[roll_greater])
    city = serializers.CharField(max_length=100)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)

    def update(self,instance,validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    #Validate ROLL field
    #Field level validation

    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value  

    #Object level validation

    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data
