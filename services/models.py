from django.db import models

# Create your models here.
class Services(models.Model):
    titre = models.CharField(max_length=30)
    description = models.TextField()
    icon = models.CharField(max_length=30)
