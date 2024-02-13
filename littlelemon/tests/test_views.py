from collections import OrderedDict
from django.test import TestCase
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer
import datetime

class MenuViewTest(TestCase):
    def setUp(self):
        # Use the setup() method to add a few test instances of the Menu model.
        self.item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = Menu.objects.create(title="Chocolate cake", price=110.98, inventory=12)
        self.item3 = Menu.objects.create(title="Carrot soup", price=110.98, inventory=1)
        
    def tearDown(self):
        Menu.objects.all().delete()
    
    def test_get_all(self):
        # retrieve all the Menu objects added for the test purpose.
        items = Menu.objects.all()

        # serialize the retrieved objects
        serialized_data = MenuSerializer(items, many=True).data
        for record in serialized_data:
            del record["id"]

        # Define the expected queryset of Menu Items
        expected_queryset = [
            OrderedDict([('title', 'IceCream'), ('price', "80.00"), ('inventory', 100)]),
            OrderedDict([ ('title', 'Chocolate cake'), ('price', "110.98"), ('inventory', 12)]),
            OrderedDict([ ('title', 'Carrot soup'), ('price', "110.98"), ('inventory', 1)])
        ]
        
        # Check if the serialized data matches the expected queryset
        self.assertEqual(serialized_data, expected_queryset)

class BookingViewTest(TestCase):
    def setUp(self):
        # Use the setup() method to add a few test instances
        self.booking_date1 = datetime.datetime.strptime("2026-02-13 06:18:00", "%Y-%m-%d %H:%M:%S" ).replace(tzinfo=datetime.timezone.utc)
        self.item1 = Booking.objects.create(name="Lana Mac", no_of_guests=3, booking_date=self.booking_date1)
        
        self.booking_date2 = datetime.datetime.strptime("2026-09-22 16:30:00", "%Y-%m-%d %H:%M:%S" ).replace(tzinfo=datetime.timezone.utc)
        self.item2 = Booking.objects.create(name="Peter7Y677YHUIHJK@jkj", no_of_guests=31, booking_date=self.booking_date2)
        
        self.booking_date3 = datetime.datetime.strptime("2029-11-02 12:15:00", "%Y-%m-%d %H:%M:%S" ).replace(tzinfo=datetime.timezone.utc)
        self.item3= Booking.objects.create(name="7897897_Bennington", no_of_guests=11, booking_date=self.booking_date3)
        
    def tearDown(self):
        Booking.objects.all().delete()
    
    def test_get_all(self):
        # retrieve all the objects added for the test purpose.
        items = Booking.objects.all()

        # serialize the retrieved objects
        serialized_data = BookingSerializer(items, many=True).data
        for record in serialized_data:
            del record["id"]

        # Define the expected queryset
        expected_queryset = [
            OrderedDict([('name', "Lana Mac"), ('no_of_guests', 3), ('booking_date', '2026-02-13T06:18:00Z')]),
            OrderedDict([ ('name', "Peter7Y677YHUIHJK@jkj"), ('no_of_guests', 31), ('booking_date', '2026-09-22T16:30:00Z')]),
            OrderedDict([ ('name', "7897897_Bennington"), ('no_of_guests', 11), ('booking_date', '2029-11-02T12:15:00Z')])
        ]
        
        # Check if the serialized data matches the expected queryset
        self.assertEqual(serialized_data, expected_queryset)
