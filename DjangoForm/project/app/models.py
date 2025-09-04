from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    image=models.ImageField(upload_to="img/")
    file=models.FileField(upload_to="files/")