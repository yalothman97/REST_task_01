from .models import Flight, Booking
import datetime
from django.utils import timezone
from rest_framework.generics import ListAPIView
from .serializers import FlightSerializer, BookingSerializer

class Flights(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class Booking(ListAPIView):
	queryset = Booking.objects.filter(date__gt=datetime.date.today())
	serializer_class = BookingSerializer


