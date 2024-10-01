from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),  # Главная страница с инвентарем
    path('add/', views.add_inventory_item, name='add_inventory_item'),  # Страница для добавления инвентаря
]
