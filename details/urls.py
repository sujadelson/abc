from .views import *
from django.urls import path  
      
urlpatterns = [  
    path('basic/', StudentView.as_view()),
    path('basic/<int:pk>', StudentDetailView.as_view()), 
    path('mark/', MarkView.as_view()) ,
    path('mark/<int:pk>', MarkDetailView.as_view()), 
    path('detail/', FullDetailView.as_view()) ,
    path('detail/<int:pk>', DetailView.as_view()),
    ]   