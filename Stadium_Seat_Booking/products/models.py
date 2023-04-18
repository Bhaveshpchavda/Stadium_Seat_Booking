from email.policy import default
from sys import maxsize
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=1000)
    summary = models.TextField()
    features = models.BooleanField(null=True)