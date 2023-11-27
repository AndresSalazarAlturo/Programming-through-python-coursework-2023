"""
Create a room described "description". Initially, it has no exits. The
'description' is something like 'kitchen' or 'an open court yard'.
"""
from my_exceptions import NotInBackpackError, WrongPassword, NotExistingRoom
from text_ui import TextUI

class Room:

    def __init__(self, description, locked = None, password=None):
        """
            Constructor method.
        :param description: Text description for this room
        :param locked: Boolean that represents if a rooms is locked by card or not
        """
        self.description = description
        self.locked = locked
        self.password = password
        self.textUI_room = TextUI()
        self.exits =        {}          # Dictionary
        self.room_items =   {}          # Dictionary

    def set_exit(self, direction, neighbour):
        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room).
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour

    def add_item_to_room(self, item):
        """
            Add the item to room_items that are stored in a list.
            All item are objects from item class.
        :param item: The item in the room
        :return: None
        """

        self.room_items[item.item_name] = item

    def can_enter(self, backpack, password = ""):
        """
            Allow access to a room locked by object or password
        :param backpack: Backpack object
        :param next_room: Next room object
        :return: True to allow access or False when wrong password or object not in backpack
        """
        if self.locked is not None:
            try:
                if self.locked == "card" and "card" not in backpack.contents:
                    raise NotInBackpackError("card", "Not in backpack")
                elif self.locked == "card2" and "card2" not in backpack.contents:
                    raise NotInBackpackError("card2", "Not in backpack")
                else:
                    return True
            except NotInBackpackError:
                return False

        if self.password is not None:
            try:
                if self.password == password:
                    return True
                else:
                    raise WrongPassword("Wrong password, try again")
            except WrongPassword:
                return False
            
    def allow_teleport(self, backpack, game_rooms):
        """
            Allow teleportation with an specific object
            :param backpack: Player backpack
            :param player_current_room: Player's current room, is the room object
            :param game_rooms: Dictionary with all rooms, key: string name; value: room object
            :return: True or False depending if the object is in the backpack
        """
        try:
            if "stone" not in backpack.contents:
                raise NotInBackpackError("stone", "no in backpack")
            else:
                print("Type your destination: ")
                destination, second_word = self.textUI_room.get_command()
                try:
                    if destination not in game_rooms:
                        raise NotExistingRoom(destination, "does not exists")
                    else:
                        next_room = game_rooms.get(destination)
                        player_current_room = next_room
                        return player_current_room
                except NotExistingRoom:
                    print("Try an existing room")
        except NotInBackpackError:
            return False

    def get_room_items(self):
        """
            Print the items in the room
        """
        for item, feature in self.room_items.items():
            print(f'The items are: {item}, description: {feature.feature}')

    def get_short_description(self):
        """
            Fetch a short text description.
        :return: text description
        """
        return f'You are in {self.description}'

    def get_long_description(self):
        """
            Fetch a longer description including available exits.
        :return: text description
        """
        return f'Location: {self.description}, Exits: {self.get_exits()}.'

    def get_exits(self):
        """
            Fetch all available exits as a list.
        :return: list of all available exits
        """
        all_exits = list(self.exits.keys())
        return all_exits

    def get_exit(self, direction):
        """
            Fetch an exit in a specified direction.
        :param direction: The direction that the player wishes to travel
        :return: Room object that this direction leads to, None if one does not exist
        """
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None
