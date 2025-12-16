from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourViewSet, BookingViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'tours', TourViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]