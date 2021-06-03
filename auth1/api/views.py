from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# with the help of basciauthentication and IsAuthenticated class any registered user can access API
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    #Following are permission classes
    #IsAuthenticated - Any registered user
    #AllowAny - Any registered/unregistered user
    #IsAdminUser - Only user with is_staf=True