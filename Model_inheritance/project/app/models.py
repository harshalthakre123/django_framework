from django.db import models

# Create your models here.

class CommonField(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    # Abstract model Inheritance:--
    # class Meta:
    #     abstract=True

class Students(CommonField):
    fees=models.IntegerField()

class Faculty(CommonField):
    department=models.CharField(max_length=50)
    contact=None

class MainModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    

class ProxyModel(MainModel):
    # proxy model Inheritance:--
    class Meta:
        proxy=True

