from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('otp',views.otp),
    path('home', views.home),
]