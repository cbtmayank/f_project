from django.db import models

# Create your models here.

class svmStudent(models.Model):
    student_id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    mobile=models.IntegerField(default=0)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)

    class Meta:
        db_table="svm_student"

