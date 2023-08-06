"""
URL configuration for studentsProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

app_name= 'students'
urlpatterns = [
    path('reg/', views.regStudents, name='reg'),
    path('regCon/', views.regConStudents, name='regCon'),
    path('all/', views.readStudentAll, name='stuAll'),
    path('<str:name>/det/', views.detStudent, name='stuDet'),
    path('<str:name>/mod/', views.readStudentOne, name='stuMod'),
    path('modCon/', views.modConStudent, name='modCon'),
    path('<str:name>/del', views.delConStudent, name='stuDel'),
]
