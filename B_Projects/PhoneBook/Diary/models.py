from django.db import models
 
# Create your models here for Python Contact Book project.
class Contact(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    Email=models.EmailField()
    ContactNumber=models.CharField(max_length=10)