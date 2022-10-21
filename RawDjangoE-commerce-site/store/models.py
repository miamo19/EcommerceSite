from django.db import models

# Create your models here.
from django.urls import reverse

"""
Product
-Nom
-Prix
-la quantite en stock
-Desccription
-Image

"""

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products", blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return reverse('products', kwargs={"slug": self.slug})
