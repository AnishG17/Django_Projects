from django.contrib import admin
from django.urls import path
from django.urls import path
from sender import views

urlpatterns = [
    path('', views.index,name='index'),
]
