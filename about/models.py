from django.db import models

# Create your models here.

class About(models.Model):
    birthday = models.CharField(max_length=30)
    website = models.URLField()
    phone = models.IntegerField(max_length=10)
    city = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    degree = models.CharField(max_length=30)
    email = models.EmailField()
    freelance = models.CharField(max_length=100)
