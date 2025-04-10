from django.urls import path
from . import views

urlpatterns = [
    path('fb/', views.feedback, name='feedback'),
]