from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('appointments/new/', views.create_appointment, name='create_appointment'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/new/', views.create_client, name='create_client'),
    path('trainers/', views.trainer_list, name='trainer_list'),
    path('trainers/new/', views.create_trainer, name='create_trainer'),
    path('sessions/', views.training_session_list, name='training_session_list'),
    path('sessions/new/', views.create_training_session, name='create_training_session'),
]
