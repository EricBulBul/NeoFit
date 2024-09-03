from django.shortcuts import render

def home(request):
    # Обрабатываем запрос и возвращаем главную страницу
    return render(request, 'main/home.html')
