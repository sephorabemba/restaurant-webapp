from collections import OrderedDict
from django.test import TestCase
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Use the setup() method to add a few test instances of the Menu model.
        self.item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = Menu.objects.create(title="Chocolate cake", price=110.98, inventory=12)
        self.item3 = Menu.objects.create(title="Carrot soup", price=110.98, inventory=1)
        
    def tearDown(self):
        pass
    
    def test_get_all(self):
        # retrieve all the Menu objects added for the test purpose.
        items = Menu.objects.all()

        # serialize the retrieved objects
        serialized_data = MenuSerializer(items, many=True).data
        
        # Define the expected queryset of Menu Items
        expected_queryset = [
            OrderedDict([('id', 2), ('title', 'IceCream'), ('price', "80.00"), ('inventory', 100)]),
            OrderedDict([('id', 3), ('title', 'Chocolate cake'), ('price', "110.98"), ('inventory', 12)]),
            OrderedDict([('id', 4), ('title', 'Carrot soup'), ('price', "110.98"), ('inventory', 1)])
        ]
        
        # Check if the serialized data matches the expected queryset
        self.assertEqual(serialized_data, expected_queryset)
