from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('payments/', views.payment_list, name='payment_list'),
    path('income-report/', views.income_report, name='income_report'),
    path('add-payment/', views.add_payment, name='add_payment'),
]