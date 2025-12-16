from django.contrib import admin
from .models import User, Tours, Booking, Payment

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email', 'role', 'date_joined')

@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ('tour_name', 'category', 'tour_price', 'created_at')
    search_fields = ('tour_name', 'category')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'user', 'tour', 'travel_date', 'book_status')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'booking', 'amount', 'pay_status', 'paid_at')