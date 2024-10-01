from django.urls import path
from .views import client_list, add_client

app_name = 'users'

urlpatterns = [
    path('clients/', client_list, name='client_list'),
    path('clients/add/', add_client, name='add_client'),
]
