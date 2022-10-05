from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    contact=models.IntegerField(max_length=10)
    age= models.IntegerField() 
