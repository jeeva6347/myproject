from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    USER={
        (1,'admin'),
    }
    user_type=models.CharField(choices=USER,max_length=50,default=1)
    profile_pic=models.ImageField(upload_to='media/profile_pic')


    
class Directory(models.Model):
    fullname=models.CharField(max_length=200)
    profession=models.CharField(max_length=200)
    email=models.EmailField(null=True, blank=True, unique=True)
    mobilenumber=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    address=models.TextField(max_length=200)
    status=models.CharField(max_length=1)
    creationdate=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    profile=models.ImageField(upload_to="images/",blank=True,null=True,default='images/default.jpg')
   
    
    def __str__(self):
        return self.fullname


    


