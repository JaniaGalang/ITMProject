from django.contrib import admin
from django.urls import include, path
from parking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('parking.urls')),
    path('thank_you_reservation/<int:reservation_id>/', views.thank_you_reservation, name='thank_you_reservation'),
    path('thank_you_cancellation/', views.thank_you_cancellation, name='thank_you_cancellation'),
]
