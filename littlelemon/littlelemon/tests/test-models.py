from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title= "cherry", price= 90, inventory=100)
        self.assertEqual(item, "ice cream : 80")