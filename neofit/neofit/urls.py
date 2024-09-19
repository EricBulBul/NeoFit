from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Подключаем маршруты из приложения main
    path('appointments/', include('appointments.urls', namespace='appointments')),
    path('attendance/', include('attendance.urls', namespace='attendance')),
    path('finance/', include('finance.urls', namespace='finance')),
    path('inventory/', include('inventory.urls', namespace='inventory')),
    path('staff/', include('staff.urls', namespace='staff')),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
