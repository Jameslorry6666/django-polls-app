#myapp/urls.py

from django.urls import path 
from . import views



urlpatterns = [
    path('message/', views.myapp_message, name='myapp_message'),
]