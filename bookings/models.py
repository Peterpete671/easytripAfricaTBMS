from django.db import models
from django.contrib.auth.models import AbstractUser

#User model

class User(AbstractUser):
    role = models.CharField(max_length=50, default='customer')
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
#Tours Model

class Tours(models.Model):
    tour_id = models.AutoField(primary_key=True)
    tour_name = models.CharField(max_length=255)
    tour_description = models.TextField()
    tour_days = models.IntegerField()
    tour_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tours/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tour_name
    
#Booking Model

class Booking(models.Model):
    book_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)
    travel_date = models.DateField()
    book_status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return f"Booking, {self.book_id} - {self.username}"
    
#Payment Model

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=100)
    pay_status = models.CharField(max_length=50, default='Pending')
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Payment {self.payment_id}"