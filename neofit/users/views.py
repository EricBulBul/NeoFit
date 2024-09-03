from django.shortcuts import render

def index(request):
    return render(request, 'users/index.html')

def user_profile(request):
    return render(request, 'users/user_profile.html')

