from django.urls import path;
from . import views;
from . import maj;

urlpatterns= [
    path('',views.go,name="go"),
    path('pre',maj.predict,name='pre')
]