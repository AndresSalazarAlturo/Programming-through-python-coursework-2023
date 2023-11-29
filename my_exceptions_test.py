import unittest
from room import *
from items import Item
from backpack import Backpack
from my_exceptions import *

class TestException(unittest.TestCase):

    def setUp(self):
        """
            Runs prior to unit test
        """
        self.room1 = Room("room1")
        self.room2 = Room("room2")
        self.room3 = Room("room3", locked="card")

        self.item1 = Item("card", "does something")
        self.item2 = Item("code", 1234)

        self.backpack = Backpack(4)

        self.room1.add_item_to_room(self.item1)
        self.room1.add_item_to_room(self.item2)
        # self.room1.add_item_to_room(self.item3)
        # self.room1.add_item_to_room(self.item4)

    def tearDown(self):
        """
            Clear the variables for the next test
        """

        self.room1 = None
        self.room2 = None
        self.room3 = None

        self.item1 = None

        self.backpack.contents.clear()

    def test_1(self):
        # self.assertRaises()     ##Look documentation
        self.backpack.add_item(self.room1.room_items[self.item1.item_name])
        with self.assertRaises(NotInBackpackError):
            self.backpack.remove_item(self.item2.item_name)