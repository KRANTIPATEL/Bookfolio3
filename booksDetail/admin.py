from django.contrib import admin
from booksDetail.models import BooksDetail

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_title','book_imglink','book_des','book_author','book_releaseDate')

admin.site.register(BooksDetail,BookAdmin)



# Register your models here.
