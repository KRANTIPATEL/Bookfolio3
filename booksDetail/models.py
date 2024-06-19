from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField


class BooksDetail(models.Model):
    book_title = models.CharField(max_length=50)
    book_imglink = models.CharField(max_length=300) 
    book_des = models.TextField()
    book_author = models.CharField(max_length=50)
    book_releaseDate = models.CharField(max_length=20)
    book_slug =AutoSlugField(populate_from = 'book_title',unique=True,null=True,default=None)

# Create your models here.
