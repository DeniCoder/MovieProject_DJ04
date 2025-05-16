from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feedback/', views.feedback, name='feedback'),
    path('new_feedback/', views.new_feedback, name='new_feedback'),
]