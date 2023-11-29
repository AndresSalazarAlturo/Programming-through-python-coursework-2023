import unittest
from room import *
from items import Item
from backpack import Backpack

class TestRoom(unittest.TestCase):

    def setUp(self):
        """
            Runs prior to unit test
        """
        self.room1 = Room("room1")
        self.room2 = Room("room2")
        self.room3 = Room("room3", locked="card")

        self.item1 = Item("card", "does something")

        self.backpack = Backpack(4)

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
        ##Test add exits to rooms
        self.assertTrue(self.room1.set_exit("north", self.room2))
        self.assertTrue(self.room2.set_exit("south", self.room3))
        self.assertEqual(self.room2.get_number_of_exits(), 1)

        ##Test add items to rooms
        self.assertTrue(self.room2.add_item_to_room(self.item1))
        self.assertEqual(self.room2.get_number_of_room_items(), 1)

        ##Test can_enter - No object in backpack
        self.assertFalse(self.room3.can_enter(self.backpack))

        ##Test can_enter - Object in backpack
        self.backpack.add_item(self.item1)
        self.assertTrue(self.room3.can_enter(self.backpack))