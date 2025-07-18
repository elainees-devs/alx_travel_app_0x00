from rest_framework import serializers
from .models import Property, Booking

# ---------------------------------------------
# Serializer for the Property model (called "Listing" in the API)
# ---------------------------------------------
class ListingSerializer(serializers.ModelSerializer):
    """
    Converts Property model instances to JSON and vice versa.
    """
    class Meta:
        model = Property
        fields = ['id', 'title', 'description', 'location', 'price_per_night']
        # 'id' is included to identify each listing in API responses


# ---------------------------------------------
# Serializer for the Booking model
# ---------------------------------------------
class BookingSerializer(serializers.ModelSerializer):
    """
    Converts Booking model instances to JSON and vice versa.
    """
    class Meta:
        model = Booking
        fields = ['id', 'user', 'property', 'check_in', 'check_out']
        # 'user' and 'property' are represented by their IDs by default
        # If needed, nested serializers can be added to show detailed info
