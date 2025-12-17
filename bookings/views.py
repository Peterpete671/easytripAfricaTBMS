from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, status, serializers as drf_serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import User

from .models import Tours, Booking, Payment
from .serializers import UserSerializer, TourSerializer, BookingSerializer, PaymentSerializer

from rest_framework_simplejwt.tokens import RefreshToken


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Allows access to Admin
    Intended for profile endpoints
    """
    def has_object_permission(self, request, view, obj):
        return bool(request.user and (request.user_is_staff or obj == request.user))
    
class IsBookingOwnerOrAdmin(permissions.BasePermission):
    """
    Allows access only to the booking owner or admin
    """
    def has_object_permission(self, request, view, obj):
        return bool(request.user and (request.user.is_staff or obj.user == request.user))
    

#Tours ViewSet
class TourViewSet(viewsets.ModelViewSet):
    """
    /api/tours
    GET: list(paginated), supports search, filtering, and ordering
    POST: Create(admin only)
    GET/{id}/: retrieve
    PUT/PATCH/DELETE: Admin only
    """
    queryset = Tours.objects.all()
    serializer_class = TourSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'tour_price', 'tour_days']
    search_fields = ['tour_price', 'tour_name','created_at']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return super().get_permissions()
    
#Bookings ViewSet
class BookingViewSet(viewsets.ModelViewSet):
    """
    /api/bookings/
    POST: create booking, user authenticated
    GET: admin -> all, user -> own
    DELETE/{id}/: Owner cancel or admin override
    To prevent duplicate booking by same user for same tour, default status = 'pending'
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all
        return Booking.objects.filter(user=user)
    
    def get_permissions(self):
        #Object level permission for retrieving, updating or destroying
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsBookingOwnerOrAdmin()]
        return super().get_permissions()
    
    def perform_create(self, serializer):
        user = self.request.user
        tour = serializer.validated_data.get('tour')
        if tour is None:
            raise drf_serializers.ValidationError({"tour": "This field is required."})
        
        if Booking.objects.filter(user=user, tour=tour).exists():
            raise drf_serializers.ValidationError("You already have a booking for this tour.")
        
        serializer.save(user=user, book_status='pending')


#Payment ViewSet
class PaymentViewSet(viewsets.ModelViewSet):
    """
    /api/payments/
    All poayment endpoints require authentication
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        #All authenticated users can interact
        return super().get_permissions()
    
#User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    """
    /api/users/
    POST: Create user, admin only
    GET(list): Admin only, paginated
    GET/{id}/: Admin, owner
    PUT/PATCH/{id}/: Admin or owner
    DELETE/{id}/: Admin only
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['list', 'create', 'destroy']:
            return [IsAdminUser()]
        if self.action in ['retrieve', 'update', 'partial_update']:
            return [IsOwnerOrAdmin()]
        return super().get_permissions()
    
#Logout View
class LogoutView(APIView):
    """
    POST /api/auth/logout/
    Body: {"refresh": "<refresh_token>"}
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({"detail": "Refresh token required."},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout Successful."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail":"Invalid or expired token."},
                            status=status.HTTP_400_BAD_REQUEST)