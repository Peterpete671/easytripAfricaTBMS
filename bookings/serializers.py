from rest_framework import serializers
from .models import User, Tours, Booking, Payment
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role', 'profile_picture', 'date_joined')
        read_only_fields = ['id', 'date_joined']
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create_user(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = '__all__'
        read_only_fields = ['tour_id', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tour = TourSerializer(read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user',
        write_only=True
    )
    tour_id = serializers.PrimaryKeyRelatedField(
        queryset=Tours.objects.all(),
        source='tour',
        write_only=True
    )

    class Meta:
        model = Booking
        fields = [
            'book_id',
            'user',
            'tour',
            'user_id',
            'tour_id',
            'booking_date',
            'travel_date',
            'book_status'
        ]
        read_only_fields = ['book_id', 'booking_date']

class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(read_only=True)

    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(),
        source='booking',
        write_only=True
    )
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['payment_id', 'paid_at']