from django.shortcuts import render
from .serializers import *
from .models import *
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets

# Create your views here.

class svmStudentViewSet(viewsets.ModelViewSet):

    def createStudent(self, request):
        try:
            data = request.data
            serializers = svmStudentSerializers(data=data)

            if serializers.is_valid():
                serializers.save()

                return JsonResponse({'message :','data submitted succesfully','payload',serializers.data})
            
            return JsonResponse({'message :','invalid data ','errors',serializers.errors})

        except Exception as ex:

            return JsonResponse({'message ':f'somthing went wrong. {ex}'})

            

