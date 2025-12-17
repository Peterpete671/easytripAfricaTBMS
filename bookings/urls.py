from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourViewSet, BookingViewSet, PaymentViewSet, UserViewSet, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'tours', TourViewSet, basename='tour')
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/logout/', LogoutView.as_view(), name='token_logout'),


    path('api/', include(router.urls)),
]