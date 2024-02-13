from django.db import models


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveSmallIntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} : {str(self.no_of_guests)} : {str(self.booking_date)}"


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.title} : {str(self.price)}"
