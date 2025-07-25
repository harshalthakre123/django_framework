from django.db import models

# Create your models here.

class Students(models.Model):
    first_name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    image=models.ImageField(upload_to="img/")
    document=models.FileField(upload_to="file/")
    password=models.CharField(max_length=25)
    def __str__(self):
        return self.first_name+' '+self.email+' '+str(self.contact)












# ORM(object relational mapper)