from django.db import models
from django.conf import settings

# ---------------------------------------------
# Property model: represents a rental property listing
# ---------------------------------------------
class Property(models.Model):
    """
    Represents a rental property listing.
    """
    title = models.CharField(max_length=255)           # Name of the listing
    description = models.TextField()                   # Detailed description of the property
    location = models.CharField(max_length=255)        # Address or coordinates of the property
    price_per_night = models.DecimalField(
        max_digits=10, decimal_places=2)               # Rental price per night (e.g., 99.99)

    def __str__(self):
        # Return a human-readable representation of the property
        return self.title


# ---------------------------------------------
# Booking model: links a user to a property for specific dates
# ---------------------------------------------
class Booking(models.Model):
    """
    Represents a booking made by a user for a property.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,                      # Reference to the User model (guest)
        on_delete=models.CASCADE,                      # Delete booking if user is deleted
        related_name='bookings'                        # Allows reverse lookup: user.bookings.all()
    )

    property = models.ForeignKey(
        'Property',                                    # Reference to the booked property
        on_delete=models.CASCADE,                       # Delete booking if property is deleted
        related_name='bookings'                         # Allows reverse lookup: property.bookings.all()
    )

    check_in = models.DateField()                       # Start date of stay
    check_out = models.DateField()                       # End date of stay

    def __str__(self):
        # Return a readable summary of the booking
        return f"Booking #{self.id} by {self.user} for {self.property}"


# ---------------------------------------------
# Review model: a user's review and rating for a property
# ---------------------------------------------
class Review(models.Model):
    """
    Represents a user's review of a property.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,                       # Reference to the reviewer (User)
        on_delete=models.CASCADE,                        # Delete review if user is deleted
        related_name='reviews'                           # Allows reverse lookup: user.reviews.all()
    )

    property = models.ForeignKey(
        'Property',                                     # Reference to the reviewed property
        on_delete=models.CASCADE,                        # Delete review if property is deleted
        related_name='reviews'                            # Allows reverse lookup: property.reviews.all()
    )

    rating = models.PositiveSmallIntegerField()          # Numerical rating (e.g., 1-5)
    comment = models.TextField(blank=True)               # Optional text review

    def __str__(self):
        # Return a readable summary of the review
        return f"Review by {self.user} for {self.property} (Rating: {self.rating})"
