from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('studentDashboard', views.display_studentdashboard, name='display_studentdashboard')
]
