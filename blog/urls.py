from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome"),
    path('about/' ,views.about , name= 'AboutUs' ),
    path('contact/' ,views.contact , name= 'Contact' ),
]
