from .views import StudentView  ,StudentDetailView
from django.urls import path  
      
urlpatterns = [  
    path('basic/', StudentView.as_view()) ,
    path('basic/<int:pk>', StudentDetailView.as_view()) 
    ]   