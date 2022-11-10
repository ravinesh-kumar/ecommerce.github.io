from django.db import models

# Create your models here.
class loginids(models.Model):
    username=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    password=models.CharField(max_length=500)
    

class contactdb(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=500)
    subject=models.CharField(max_length=500)
    message=models.CharField(max_length=5000)
