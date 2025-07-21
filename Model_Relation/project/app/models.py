from django.db import models

# Create your models here.

class Aadhar(models.Model):
    a_no=models.IntegerField(unique=True)
    gen_date=models.DateField()
    
class Students(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    city=models.CharField()
    a_no=models.OneToOneField(Aadhar, on_delete=models.PROTECT, related_name='stu_info')


#one to many==================
class Department(models.Model):
    d_name=models.CharField(max_length=50)

class Students1(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    depart=models.ForeignKey(Department, on_delete=models.PROTECT, related_name="student_info")



# Many to many relation================================================

class Fuel(models.Model):
    f_name=models.CharField(max_length=50, unique=True)

class Vehicle(models.Model):
    v_name=models.CharField(max_length=50)
    f_name=models.ManyToManyField(Fuel, related_name="vehicle")