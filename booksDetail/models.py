from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField

# Create your models here.

class BooksDetail(models.Model):
    book_title = models.CharField(max_length=50)
    book_imglink = models.CharField(max_length=300)
    book_des = models.TextField()
    book_author = models.CharField(max_length=50)
    book_releaseDate = models.CharField(max_length=20)
