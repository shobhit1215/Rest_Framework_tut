"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from movies.views import MovieViewSet,ActionMovie
from api import views
from postapi import views as student_create_view
from crudapi import views as crud_views
#urls for movies
router = routers.SimpleRouter()
router.register('movies',MovieViewSet)
router.register('action',ActionMovie)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    #urls for api
    path('stuinfo/<int:pk>',views.student_detail),
    path('stulist/',views.student_list),
    # urls for postapi
    path('stucreate/',student_create_view.student_create),
    #For CRUD api
    path('studentapi/',crud_views.student_api),


]
