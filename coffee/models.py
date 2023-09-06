from django.db import models
#from coffee.models import BaseModel, Product

# Create your models here.

class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)
  