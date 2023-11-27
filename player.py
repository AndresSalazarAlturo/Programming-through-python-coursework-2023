"""
Create the player objects that whose attributes are:
    Name
    Backpack
    Current position
"""

class Player:

    def __init__(self, name=None, backpack=None, current_room=None):
        """
            Constructor method.
        :param name: String with player's name
        :param backpack: Object from class Backpack
        :param current_position: Current player's position, object from Room class
        """
        self.name = name
        self.backpack = backpack
        self.current_room = current_room
