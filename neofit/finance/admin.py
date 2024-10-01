from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('client', 'amount', 'payment_date', 'method', 'category')
    search_fields = ('client__last_name', 'client__first_name')

admin.site.register(Payment, PaymentAdmin)