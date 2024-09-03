from django.shortcuts import render

# Убедитесь, что у вас есть функция с именем index
def index(request):
    # Примерный контент функции, измените по необходимости
    return render(request, 'finance/index.html')
