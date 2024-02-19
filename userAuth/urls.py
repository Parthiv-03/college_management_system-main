from django.contrib import admin
from django.urls import path, include
import CMS
from . import views

urlpatterns = [
    path('', views.user_authantication, name='login'),
    path('/', include('studentPanel.urls'), name='studentPanel')
]
