# from unittest import result
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    resume = models.ImageField(upload_to='picture', null=True)