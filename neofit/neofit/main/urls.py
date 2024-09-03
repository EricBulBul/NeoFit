from django.urls import path
from . import views

app_name = 'main'  # Указываем пространство имен для приложения

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
]