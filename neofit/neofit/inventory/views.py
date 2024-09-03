from django.shortcuts import render

def index(request):
    return render(request, 'inventory/index.html')

def item_list(request):
    return render(request, 'inventory/item_list.html')
