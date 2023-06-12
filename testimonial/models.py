from django.db import models

# Create your models here.
class Testimonial(models.Model):
    description = models.TextField()
    photo = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)

    