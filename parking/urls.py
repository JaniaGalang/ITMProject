from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('locations/', views.choose_location, name='choose_location'),
    path('locations/<int:location_id>/', views.view_places, name='view_places'),
    path('thank_you_reservation/<int:reservation_id>/', views.thank_you_reservation, name='thank_you_reservation'),
    path('thank_you_cancellation/', views.thank_you_cancellation, name='thank_you_cancellation'),
    path('history/', views.history_view, name='history'),
]
