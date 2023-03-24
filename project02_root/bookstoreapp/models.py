from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=999)
    author_fname = models.CharField(max_length=999)
    author_lname = models.CharField(max_length=999)
    release_year = models.DecimalField(max_digits=4, decimal_places=0)
    price = models.DecimalField(max_digits=5, decimal_places=2) # number from 0.0-999.99
    synopsis = models.TextField()
