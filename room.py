"""
Create a room described "description". Initially, it has no exits. The
'description' is something like 'kitchen' or 'an open court yard'.
"""
from src.my_exceptions import NotInBackpackError, WrongPassword, NotExistingRoom
from src.text_ui import TextUI

class Room:

    def __init__(self, description, locked = None, password=None):
        """
            Constructor method.
        :param description: Text description for this room
        :param locked: String that represents if a rooms is locked by card or other object
        :param password: String that is the password to go in the room
        """
        self.description = description
        self.locked = locked
        self.password = password
        self.textUI_room = TextUI()
        self.exits =        {}          # Dictionary
        self.room_items =   {}          # Dictionary
        self.hidden_items = {}          # Dictionary

    def set_exit(self, direction, neighbour):
        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room).
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour
        return True

    def add_item_to_room(self, item):
        """
            Add the item to room_items that are stored in a dictionary.
            All item are objects from item class.
        :param item: The item in the room
        :return: True
        """

        self.room_items[item.item_name] = item
        return True

    def remove_item_to_room(self, item):
        """
            Remove an item to room. Is used when the player pick an item from the room
        :param item: The item picked by the player
        :return: True when remove the item
        """
        self.room_items.pop(item)
        print(f"{item} is no longer in the room")
        return True

    def add_hidden_item_to_room(self, item):
        """
            Add the hidden item to room_items that are stored in a dictionary.
            All item are objects from item class.
        :param item: The item in the room
        :return: True
        """

        self.hidden_items[item.item_name] = item
        return True

    def can_enter(self, backpack, password = "", game_rooms = None, next_room = None, dining_room_lock = None):
        """
            Allow access to a room locked by object or password
        :param backpack: Backpack object
        :param next_room: Next room object
        :return: True to allow access or False when wrong password or object not in backpack
        """

        if self.locked is not None:
            ##Get the office room items to know if the statue is there
            office_items = game_rooms["office"]
            dining_room_lock = dining_room_lock["dining_room"]
            try:
                if self.locked == "card" and "card" not in backpack.contents:
                    print("The object 'card' is needed to access this room")
                    raise NotInBackpackError("card", "Not in backpack")
                
                elif self.locked == "card2" and "card2" not in backpack.contents:
                    print("The object 'card2' is needed to access this room")
                    raise NotInBackpackError("card2", "Not in backpack")
                
                elif self.locked == "statue" and "statue" not in office_items.room_items:
                    print("The statue is not pressing the button")
                    return False

                elif dining_room_lock.locked == True and next_room == dining_room_lock:
                    print("The room is locked, solve the figures mini_game to access")
                    return False

                elif self.locked == "key" and "key" not in backpack.contents:
                    print("The door is locked, get the key to go out")
                    return False

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
                print("The available rooms to teleport are: ")
                for i, rooms in enumerate(game_rooms.keys()):
                    print(f"{i}. {rooms}")
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
        print(f"The items are: \n")
        for item, feature in self.room_items.items():
            print(f'{item} --> description: {feature.feature}')

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
    
    def get_number_of_exits(self):
        """
            Return the number of exits in the room
        """
        all_exits = list(self.exits.keys())
        return len(all_exits)
    
    def get_number_of_room_items(self):
        """
            Return the number of items in the room
        """
        all_items = list(self.room_items.keys())
        return len(all_items)

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
