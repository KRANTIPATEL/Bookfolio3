from django.db import models

class Prices(models.Model):
    things = models.CharField(max_length=50)
    things_price = models.CharField(max_length=50)
# Create your models here.
