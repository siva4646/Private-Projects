from django.db import models # Import the models module


class Product(models.Model): # Inherit Model class
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


