from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('add/', views.add_payment, name='add_payment'),
    path('income_report/', views.income_report, name='income_report'),  # Добавьте этот путь
]