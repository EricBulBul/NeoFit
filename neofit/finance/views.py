from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentForm

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'finance/payment_list.html', {'payments': payments})


def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:payment_list')  # Перенаправление на список платежей
    else:
        form = PaymentForm()

    return render(request, 'finance/add_payment.html', {'form': form})

def income_report(request):
    return render(request, 'finance/income_report.html')