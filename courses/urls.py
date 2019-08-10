from django.urls import path, include
from . import views

urlpatterns = [
    path('classroomcourses/', views.classroomcourses_index,
         name="classroomcourses_index"),
    path('liveonlinecourses/', views.liveonlinecourses_index,
         name="liveonlinecourses_index"),

]
