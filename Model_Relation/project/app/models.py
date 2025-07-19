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