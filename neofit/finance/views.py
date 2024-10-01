from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment
from django.utils import timezone
from django.db.models import Q


def payment_list(request):
    queryset = Payment.objects.all()

    last_name = request.GET.get('last_name')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    if last_name:
        queryset = queryset.filter(client__last_name__icontains=last_name)

    if date_from:
        queryset = queryset.filter(date__gte=date_from)

    if date_to:
        queryset = queryset.filter(date__lte=date_to)

    context = {
        'payments': queryset,
        'last_name': last_name,
        'date_from': date_from,
        'date_to': date_to,
    }
    return render(request, 'finance/payment_list.html', context)

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:payment_list')  # Замените на нужное имя страницы
    else:
        form = PaymentForm()
    return render(request, 'finance/add_payment.html', {'form': form})
def income_report(request):
    # Логика для формирования отчета по доходам
    return render(request, 'finance/income_report.html')  # Создайте шаблон income_report.html