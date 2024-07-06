from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField



# Create your models here.

class bookColumn(models.Model):
    bookDB_title = models.CharField(max_length=50)
    bookDB_imglink = models.CharField(max_length=300)
    bookDB_price = models.CharField(max_length=300)

    bookDB_des = models.TextField()
    bookDB_author = models.CharField(max_length=50)
    bookDB_releaseDate = models.CharField(max_length=20)
    bookDB_slug = AutoSlugField(populate_from = 'bookDB_title',unique=True,null=True,default=None)

