from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# with the help of basciauthentication and IsAuthenticated class any registered user can access API
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [DjangoModelPermissions]
    #Following are permission classes
    #IsAuthenticated - Any registered user
    #AllowAny - Any registered/unregistered user
    #IsAdminUser - Only user with is_staf=True
    #IsAuthenticatedOrReadOnly - Authenticated(any request) Unauthenticated(safe request)
    #DjangoModelPermissions - We have to assign permission for POST,PUT,Patch to the users from admin panel
    #DjangoModelPermissionsOrAnonReadOnly - same as DjangoModelPermissions but provides aunauthenticated user with read only access 