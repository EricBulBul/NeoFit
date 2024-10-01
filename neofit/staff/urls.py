from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.staff_list, name='staff_list'),
    path('new/', views.create_staff_member, name='create_staff_member'),  # Добавляем маршрут для создания сотрудника
]
