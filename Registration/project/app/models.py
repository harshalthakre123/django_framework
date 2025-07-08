from django.db import models

# Create your models here.

class Students(models.Model):
    first_name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    image=models.ImageField(upload_to="img/")
    document=models.FileField(upload_to="file/")












# ORM(object relational mapper)