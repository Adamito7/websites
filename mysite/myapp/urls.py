from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('home/', views.form_view),
    path('timer/', views.timer_view),
]

