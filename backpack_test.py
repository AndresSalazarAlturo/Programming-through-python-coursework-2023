import unittest
from items import Item
from backpack import Backpack
from room import Room
from my_exceptions import *

class TestBackpack(unittest.TestCase):

    def setUp(self):
        """
            Runs prior to unit test
        """

        self.backpack = Backpack(3)

        self.item1 = Item("card", "does something")
        self.item2 = Item("doc", "some info")
        self.item3 = Item("key", "some key")
        self.item4 = Item("paper", "some paper")

        self.room1 = Room("room1")

        self.room1.add_item_to_room(self.item1)
        self.room1.add_item_to_room(self.item2)
        self.room1.add_item_to_room(self.item3)
        self.room1.add_item_to_room(self.item4)

    def tearDown(self):
        """
            Clear the variables for the next test
        """

        self.item1 = None
        self.item2 = None
        self.item3 = None

        self.backpack.contents.clear()

        self.room1 = None

    def test_1(self):

        ##Backpack items
        self.backpack.add_item(self.room1.room_items[self.item1.item_name])
        self.backpack.add_item(self.room1.room_items[self.item2.item_name])

        ##Test add_items
        self.assertEqual(self.backpack.get_number_of_items(),2)

        ##Test item already in backpack
        self.assertTrue(self.backpack.check_item(self.item1.item_name))
        
        ##Test add_item
        self.assertTrue(self.backpack.add_item(self.item3))
        ##Test backpack is full
        self.assertFalse(self.backpack.add_item(self.item4))

    def test_2(self):

        ##Backpack items
        self.backpack.add_item(self.room1.room_items[self.item1.item_name])
        self.backpack.add_item(self.room1.room_items[self.item2.item_name])

        ##Test remove items
        self.assertEqual(self.backpack.get_number_of_items(),2)
        self.backpack.remove_item(self.item2.item_name)
        self.assertEqual(self.backpack.get_number_of_items(),1)

        ##Test remove item not in backpack
        # self.assertFalse(self.backpack.remove_item(self.item1))