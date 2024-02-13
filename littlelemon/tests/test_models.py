from django.test import TestCase
from restaurant.models import Booking, Menu
import datetime
from decimal import Decimal

class MenuTest(TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        Menu.objects.all().delete()
    
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        output = str(item)
        expected = "IceCream : 80"
        self.assertEqual(output, expected)
        
        
    def test_update_item(self):
        item = Menu.objects.create(title="Pancake", price=12.11, inventory=100)
        item = Menu.objects.get(title="Pancake")
        item.title = "Pancake Updated"
        item.price = Decimal("19.11")
        item.inventory = 10
        item.save()
        
        item_refreshed = Menu.objects.get(title="Pancake Updated")
        self.assertEqual(item.title, item_refreshed.title)
        self.assertEqual(item.price, item_refreshed.price)
        self.assertEqual(item.inventory, item_refreshed.inventory)

class BookingTest(TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        Booking.objects.all().delete()
    
    def test_get_item(self):
        booking_date = datetime.datetime.strptime("2026-02-13 06:18:00", "%Y-%m-%d %H:%M:%S" ).replace(tzinfo=datetime.timezone.utc)
        item = Booking.objects.create(name="John Land", no_of_guests=12, booking_date=booking_date)
        output = str(item)
        expected = "John Land - 2026-02-13 06:18:00"
        self.assertEqual(output, expected)

    def test_update_item(self):
        booking_date = datetime.datetime.strptime("2026-02-15 02:38:00", "%Y-%m-%d %H:%M:%S" ).replace(tzinfo=datetime.timezone.utc)
        item = Booking.objects.create(name="Stan Paul", no_of_guests=2, booking_date=booking_date)
        item = Booking.objects.get(name="Stan Paul")
        item.name = "Stan Pauldeene"
        item.no_of_guests = 12
        item.booking_date = datetime.datetime.strptime("2026-02-18 18:00:00", "%Y-%m-%d %H:%M:%S" ).replace(tzinfo=datetime.timezone.utc)
        item.save()
        
        item_refreshed = Booking.objects.get(name="Stan Pauldeene")
        self.assertEqual(item.name, item_refreshed.name)
        self.assertEqual(item.no_of_guests, item_refreshed.no_of_guests)
        self.assertEqual(item.booking_date, item_refreshed.booking_date)
