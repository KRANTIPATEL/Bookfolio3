from django.db import models

class BooksDetail(models.Model):
    book_title = models.CharField(max_length=50)
    book_imglink = models.CharField(max_length=300) 
    book_des = models.TextField()
    book_author = models.CharField(max_length=50)
    book_releaseDate = models.CharField(max_length=20)
    # book_slug = models.FileField( upload_to="books/", max_length=250,null=True,default=None)

# Create your models here.
