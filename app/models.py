from django.db import models
from django.db.models import Sum
# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    club =  models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Coach(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    club =  models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    marked_price = models.FloatField()
    sold_price = models.FloatField( blank=True)
   

    @property
    def get_sold_price(self):
      return self.marked_price*0.95
    def save(self, *args, **kwargs):
      self.sold_price = self.get_sold_price
      super(Item, self).save(*args, **kwargs)

    def __float__(self):
       return self.sold_price

    def __str__(self):
        return self.name
