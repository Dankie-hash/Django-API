from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=150)
    symbol = models.CharField(max_length=10)
    description = models.TextField()
    sector = models.CharField(max_length=150)
    market_cap = models.FloatField()
    country = models.CharField(max_length=100)
    index = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class StockExchange(models.Model):
    name = models.CharField(max_length=150)
    mic = models.CharField(max_length=10)
    market_place = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    market_cap = models.FloatField()

    def __str__(self):
        return self.name

    



