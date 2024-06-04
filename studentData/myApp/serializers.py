from rest_framework import serializers
from .models import svmStudent

class svmStudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = svmStudent
        field = ('__all__')
