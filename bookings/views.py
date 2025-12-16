from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Tours, Booking, Payment
from .serializers import TourSerializer, BookingSerializer, PaymentSerializer
# Create your views here.

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tours.objects.all()
    serializer_class = TourSerializer
    permission_classes = [permissions.AllowAny]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]