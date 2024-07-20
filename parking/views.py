from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import Location, Spot, Reservation
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm, CancelReservationForm, ExtendTimeForm
import pytz

def home(request):
    return render(request, 'parking/home.html')

def choose_location(request):
    locations = Location.objects.all()
    locations_with_details = []

    for location in locations:
        total_capacity = location.capacity
        available_spots = Spot.objects.filter(location=location, is_available=True).count()
        locations_with_details.append({
            'location': location,
            'total_capacity': total_capacity,
            'available_spots': available_spots
        })

    return render(request, 'parking/choose_location.html', {'locations_with_details': locations_with_details})

def view_places(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    spots = Spot.objects.filter(location=location)
    total_capacity = location.capacity
    available_spots = total_capacity - spots.filter(is_available=False).count()
    reservation_form = ReservationForm()
    cancel_form = CancelReservationForm()
    
    spot_reservations = {}
    for spot in spots:
        reservation = Reservation.objects.filter(spot=spot).first()
        spot_reservations[spot.id] = reservation

    print("Spot Reservations:", spot_reservations)  # Debugging line

    if request.method == 'POST':
        if 'reserve' in request.POST:
            reservation_form = ReservationForm(request.POST)
            if reservation_form.is_valid():
                plate_number = reservation_form.cleaned_data['plate_number']
                id_number = reservation_form.cleaned_data['id_number']
                spot_id = request.POST.get('spot_id')
                spot = get_object_or_404(Spot, id=spot_id)

                # Check for existing reservation
                existing_reservation = Reservation.objects.filter(
                    plate_number=plate_number, 
                    id_number=id_number
                ).first()

                if existing_reservation:
                    messages.error(request, 'You already have an existing reservation with this plate number and ID number. Please cancel your first reservation before reserving another slot.')
                elif spot.is_available:
                    reservation = reservation_form.save(commit=False)
                    reservation.spot = spot
                    reservation.save()
                    
                    spot.is_available = False
                    spot.save()
                    
                    return redirect('thank_you_reservation', reservation_id=reservation.id)
                else:
                    messages.error(request, 'The selected spot is no longer available.')
        elif 'cancel' in request.POST:
            cancel_form = CancelReservationForm(request.POST)
            if cancel_form.is_valid():
                spot_id = request.POST.get('spot_id')
                spot = get_object_or_404(Spot, id=spot_id)
                reservation = Reservation.objects.filter(spot=spot).first()
                plate_number = cancel_form.cleaned_data['plate_number']
                id_number = cancel_form.cleaned_data['id_number']
                
                if reservation and reservation.plate_number == plate_number and reservation.id_number == id_number:
                    reservation.delete()
                    spot.is_available = True
                    spot.save()
                    return redirect('thank_you_cancellation')
                else:
                    messages.error(request, 'Plate number or ID number does not match.')

    return render(request, 'parking/view_places.html', {
        'location': location,
        'spots': spots,
        'available_spots': available_spots,
        'total_capacity': total_capacity,
        'reservation_form': reservation_form,
        'cancel_form': cancel_form,
        'spot_reservations': spot_reservations,
    })

def thank_you_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'parking/thank_you_reservation.html', {'reservation': reservation})

def thank_you_cancellation(request):
    return render(request, 'parking/thank_you_cancellation.html')

def history_view(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == '1234':
            reservations = Reservation.objects.select_related('spot__location').all()

            philippine_tz = pytz.timezone('Asia/Manila')
            for reservation in reservations:
                if reservation.date_reserved:
                    reservation.date_reserved = reservation.date_reserved.astimezone(philippine_tz)
            
            return render(request, 'parking/history.html', {'reservations': reservations})
        else:
            error_message = "Incorrect password. Please try again."
            return render(request, 'parking/password_prompt.html', {'error_message': error_message})
    return render(request, 'parking/password_prompt.html')
