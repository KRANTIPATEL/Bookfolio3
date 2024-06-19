from django.contrib import admin
from logindata.models import LoginDetails

class LoginAdmin(admin.ModelAdmin):
    list_display = ('login_email','login_pwd')
# Register your models here.
admin.site.register(LoginDetails,LoginAdmin)
