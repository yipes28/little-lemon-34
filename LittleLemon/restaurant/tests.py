from django.test import TestCase
from django.utils import timezone

# Create your tests here.
from .models import MenuItem, Booking


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertNotEqual(item, "IceCream : 80")


class BookingTest(TestCase):
    def test_booking(self):
        booking = Booking.objects.create(
            name="Bob", no_of_guests="5", booking_date="2024-02-12 12:00"
        )
        if str(booking) != "Bob : 5 : 2024-02-12 12:00":
            self.assertEqual(True, False)
