from django.test import TestCase
from restaurant.models import Booking, Menu

class MenuTest(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item_str = str(item)
        expected = "IceCream : 80"
        self.assertEqual(item_str, expected)
