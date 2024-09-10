from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-generated ID
    name = models.CharField(max_length=100)  # Name of the person making the booking
    no_of_guests = models.PositiveIntegerField()  # Number of guests
    booking_date = models.DateField()  # Date of the booking

    def __str__(self):
        return f"Booking by {self.name} on {self.booking_date}"
    

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveBigIntegerField()


    def __str__(self):
        return f'{self.title} : {(self.price)}'
