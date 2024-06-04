from django.urls import path
from myApp import views

urlpatterns = [
    
    path('std/', views.svmStudentViewSet.as_view({'POST': 'createStudent'}),name="std"),
]
