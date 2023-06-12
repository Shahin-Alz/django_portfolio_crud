from django.db import models


# Create your models here.
class Contact(models.Model):
    location = models.CharField(max_length=30)
    mail = models.EmailField()
    phone = models.PositiveIntegerField(max_length=12)
