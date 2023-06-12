from django.db import models

# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=30)
    value = models.IntegerField(max_length=2)
    