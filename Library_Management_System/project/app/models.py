from django.db import models

# Create your models here.

class Books(models.Model):
    book_name=models.CharField(max_length=50, unique=True)
    author=models.CharField(max_length=50)


class LibId(models.Model):
    lib_id=models.CharField(max_length=15, unique=True)
    issued_book=models.ManyToManyField(Books, related_name="stu_info")


class Branch(models.Model):
    branch_name=models.CharField(max_length=50, unique=True)
    


class Students(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    branch=models.ForeignKey(Branch, on_delete=models.PROTECT, related_name="stu_branch")
    lib_id=models.OneToOneField(LibId, on_delete=models.PROTECT, related_name="stu_lid")
    



    
    
    