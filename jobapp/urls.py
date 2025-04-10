from django.urls import path
from . import views

urlpatterns = [
    path('job_form/', views.candidate_registration, name='candidate_registration'),
]