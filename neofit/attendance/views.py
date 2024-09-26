from django.shortcuts import render, redirect
from .models import Attendance
from .forms import AttendanceForm
from django.utils import timezone


def attendance_list(request):
    attendances = Attendance.objects.all()

    # Получаем значения из GET-запроса
    date_filter = request.GET.get('date')
    surname_filter = request.GET.get('surname')

    # Фильтрация по дате, если указана
    if date_filter:
        attendances = attendances.filter(date=date_filter)

    # Фильтрация по фамилии клиента, если указана
    if surname_filter:
        attendances = attendances.filter(client__last_name__icontains=surname_filter)

    return render(request, 'attendance/attendance_list.html', {'attendances': attendances})

def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.date = timezone.now()  # Устанавливаем текущую дату
            attendance.save()
            return redirect('attendance:attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/mark_attendance.html', {'form': form})