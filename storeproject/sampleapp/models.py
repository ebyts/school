from django.db import models 

# Create your models here.

class detail(models.Model):
    name = models.CharField(max_length=100)
    dob= models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    phone=models.IntegerField(max_length=12)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    department=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    purpose=models.CharField(max_length=100)
    materials=models.CharField(max_length=100)


    def __str__(self):
        return self.name



    
