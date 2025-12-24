from django.db import models

# Create your models here.
class Course(models.Model):
    image=models.ImageField(upload_to="images")
    title= models.CharField(max_length=30)
    desc= models.TextField()
    price= models.IntegerField()

class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    isdelete = models. BooleanField (default = False)

    
def __str__(self):
     return self.name
