from django.contrib import admin
from cartDB.models import cartColumn

class CartAdmin(admin.ModelAdmin):
    list_display = ('item_title','item_imglink','item_des','item_author','item_releaseDate')

admin.site.register(cartColumn,CartAdmin)



# Register your models here.
