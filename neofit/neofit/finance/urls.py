from django.urls import path
from . import views

app_name = 'finance'  # Убедитесь, что это пространство имён правильно

urlpatterns = [
    path('', views.index, name='index'),  # Убедитесь, что views.index существует
    # Добавьте другие маршруты для вашего приложения здесь
]
