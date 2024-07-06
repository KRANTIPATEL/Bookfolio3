from django.contrib import admin

from bookDB.models import bookColumn

class BookDBAdmin(admin.ModelAdmin):
    list_display = ('bookDB_title','bookDB_imglink','bookDB_des','bookDB_price','bookDB_author','bookDB_releaseDate')

admin.site.register(bookColumn,BookDBAdmin)



# Register your models here.

