"""
URL configuration for BookFolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BookFolio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutus/', views.aboutUs,name="aboutus"),
    path('',views.homePage,name="home"),
    path('signin/',views.signin,name="signin"),
    path('signup/',views.signup,name="signup"),

    path('contact/', views.contact,name="contact"),
    path('gallery1/<slug>', views.gallery1),
    path('gallery/', views.gallery),


    path('services/', views.services,name="services"),

    path('userform/', views.userForm),
    path('submitform/', views.submitform,name="submitform"),
    path('calculator/', views.calculator),
    path('validationform/', views.validationForm),
    path('newsdetail/<slug>', views.newsDetail),


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)