#polls/urls.py

from django.urls import path 
from . import views


#urlpatterns = [
 #   path('message/', views.polls_message, name='polls_message'),
    # Add other polls URLs here
#]

from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('message/', views.polls_message, name='polls_message'),
]
