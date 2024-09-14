from django.db import models

# Create your models here.

class Imageslider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='imageslider/')
