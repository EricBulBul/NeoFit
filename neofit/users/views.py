from django.shortcuts import render, redirect
from appointments.models import Client
from appointments.forms import ClientForm

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'users/client_list.html', {'clients': clients})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:client_list')
    else:
        form = ClientForm()
    return render(request, 'users/add_client.html', {'form': form})
