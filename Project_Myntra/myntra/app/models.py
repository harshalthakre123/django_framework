from django.db import models

# Create your models here.

class Users(models.Model):
    f_name=models.CharField(max_length=25)
    l_name=models.CharField(max_length=25)
    email=models.EmailField()
    contact=models.IntegerField()
    password=models.CharField(max_length=25)
    def __str__(self):
        return self.f_name+" "+self.l_name
