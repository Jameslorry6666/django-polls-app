#polls/urls.py

from django.urls import path 
from . import views


urlpatterns = [
    path('message/', views.polls_message, name='polls_message'),
    # Add other polls URLs here
]