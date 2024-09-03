from django.shortcuts import render

def index(request):
    return render(request, 'staff/index.html')

def staff_list(request):
    return render(request, 'staff/staff_list.html')

