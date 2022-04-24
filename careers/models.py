from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class career(models.Model):
    career_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='picture')
    img1 = models.ImageField(upload_to='picture', null=True)
    img2 = models.ImageField(upload_to='picture', null=True)
    img3 = models.ImageField(upload_to='picture', null= True)
    description = models.TextField()
    video = models.FileField(upload_to='video', null=True, verbose_name='video')
    def __str__(self):
        return self.career_name
    
class Job(models.Model):
    company_name = models.ForeignKey(User, on_delete=models.CASCADE)
    company_description = models.TextField()
    image1 = models.ImageField(upload_to='picture', null=True)
    image2 = models.ImageField(upload_to='picture', null=True)
    image3 = models.ImageField(upload_to='picture', null=True)
    vacancy = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    def __int__(self):
        return self.company_name