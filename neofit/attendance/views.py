from django.shortcuts import render

def index(request):
    # Логика для представления главной страницы приложения attendance
    return render(request, 'attendance/index.html')

