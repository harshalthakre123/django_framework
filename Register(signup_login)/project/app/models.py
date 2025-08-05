from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    image=models.ImageField(upload_to="images/")
    document=models.FileField(upload_to="files")
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Query(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    query=models.CharField(max_length=255)
    