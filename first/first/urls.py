from django.contrib import admin
from django.urls import path, include;

urlpatterns = [
    path('',include('home.urls'),name="map"),
    path('admin/', admin.site.urls) 
]
