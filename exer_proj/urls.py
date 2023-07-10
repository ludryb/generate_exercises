"""
URL configuration for exer_proj project.

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
from app import views

urlpatterns = [
    path('', views.exercises, name='exercises'),
    path('exercises', views.exercises, name='exercises'),
    #path('exercises/', views.exercises, name='exercises'),
    path('check_exercise_1', views.check_exercise_1, name='check_exercise_1'),
    path('check_exercise_2', views.check_exercise_2, name='check_exercise_2'),
    path('check_exercise_3', views.check_exercise_3, name='check_exercise_3'),
    path('check_exercise_4', views.check_exercise_4, name='check_exercise_4'),

]


