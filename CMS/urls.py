from django.contrib import admin
from django.urls import path, include
import userAuth
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exp.urls'), name='exp'),
    path('', views.display_indexpage, name='display_indexpage'),
    path('login', include('userAuth.urls'), name='userAuth'),
    path('', include('studentPanel.urls'),name='studentPanel')
]









