from django.contrib import admin
from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('client', 'session', 'date', 'present')  # Поля для отображения в списке
    list_filter = ('date', 'session', 'present')  # Фильтры для поиска по дате, тренировке и присутствию
    search_fields = ('client__name', 'session__name')  # Поиск по имени клиента или названию тренировки
    list_editable = ('present',)  # Возможность редактирования поля присутствия в списке

admin.site.register(Attendance, AttendanceAdmin)