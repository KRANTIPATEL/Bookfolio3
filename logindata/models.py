from django.db import models

class LoginDetails(models.Model):
    login_email  = models.CharField(max_length=50)
    login_pwd = models.CharField(max_length=50)
    
# Create your models here.
