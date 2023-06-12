from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name= models.CharField(max_length=30)
    image= models.ImageField(upload_to='media/')
    

class Filter(models.Model):
    name= models.CharField(max_length=30)