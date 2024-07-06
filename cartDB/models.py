from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField

# Create your models here.

class cartColumn(models.Model):
    item_title = models.CharField(max_length=50)
    item_imglink = models.CharField(max_length=300)
    item_price = models.CharField(max_length=300)

    item_des = models.TextField()
    item_author = models.CharField(max_length=50)
    item_releaseDate = models.CharField(max_length=20)
    item_slug = AutoSlugField(populate_from = 'item_title',unique=True,null=True,default=None)
    item_quantity = models.PositiveIntegerField(default=1)

