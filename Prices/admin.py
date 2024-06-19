from django.contrib import admin
from Prices.models import Prices

class PriceAdmin(admin.ModelAdmin):
    list_display = ('things','things_price')

admin.site.register(Prices,PriceAdmin)
# Register your models here.
