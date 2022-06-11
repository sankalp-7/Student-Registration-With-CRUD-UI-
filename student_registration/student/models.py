from django.db import models
from django.forms import IntegerField

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.PositiveBigIntegerField(max_length=10)
    Class=models.IntegerField()
    marks=models.PositiveIntegerField()


