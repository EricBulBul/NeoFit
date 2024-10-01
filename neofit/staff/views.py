
from django.shortcuts import render, redirect
from .models import StaffMember
from .forms import StaffForm

def staff_list(request):
    staff_members = StaffMember.objects.all()
    return render(request, 'staff/staff_list.html', {'staff_members': staff_members})

def create_staff_member(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff:staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff/create_staff_member.html', {'form': form})

def edit_staff_member(request, pk):
    staff_member = StaffMember.objects.get(pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff_member)
        if form.is_valid():
            form.save()
            return redirect('staff:staff_list')
    else:
        form = StaffForm(instance=staff_member)
    return render(request, 'staff/edit_staff_member.html', {'form': form})
