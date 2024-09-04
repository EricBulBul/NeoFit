from django.shortcuts import render, redirect
from .models import Client, Trainer, TrainingSession, Appointment
from .forms import ClientForm, TrainerForm, TrainingSessionForm, AppointmentForm

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments:appointment_list')  # Обновлено
    else:
        form = AppointmentForm()
    return render(request, 'appointments/create_appointment.html', {'form': form})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'appointments/client_list.html', {'clients': clients})

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments:client_list')  # Обновлено
    else:
        form = ClientForm()
    return render(request, 'appointments/create_client.html', {'form': form})

def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'appointments/trainer_list.html', {'trainers': trainers})


def create_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments:trainer_list')  # Перенаправление на список тренеров после успешного сохранения
    else:
        form = TrainerForm()
    return render(request, 'appointments/create_trainer.html', {'form': form})

def training_session_list(request):
    sessions = TrainingSession.objects.all()
    return render(request, 'appointments/training_session_list.html', {'sessions': sessions})

def create_training_session(request):
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_session_list')  # Перенаправление на страницу со списком тренировок
    else:
        form = TrainingSessionForm()
    return render(request, 'appointments/create_training_session.html', {'form': form})