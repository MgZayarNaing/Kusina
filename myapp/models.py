from django.db import models

# Create your models here.

class Imageslider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='imageslider/')
    desc = models.TextField()


class About1(models.Model):
    image = models.ImageField(upload_to='about1/')
    video = models.FileField(upload_to='about1/')

class About2(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()

class About3(models.Model):
    image = models.ImageField(upload_to='about3/')
    name = models.CharField(max_length=200)

class Project(models.Model):
    years = models.CharField(max_length=200)
    customers =  models.CharField(max_length=200)
    projects = models.CharField(max_length=200)
    days = models.CharField(max_length=200)

class Menu(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='menu/')
    price = models.CharField(max_length=200)