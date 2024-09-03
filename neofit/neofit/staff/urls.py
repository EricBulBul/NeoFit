from django.urls import path
from . import views

app_name = 'staff'  # Это пространство имён для приложения

urlpatterns = [
    path('', views.index, name='index'),
    # Добавьте другие маршруты для вашего приложения здесь
]