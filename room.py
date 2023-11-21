"""
Create a room described "description". Initially, it has no exits. The
'description' is something like 'kitchen' or 'an open court yard'.
"""


class Room:

    def __init__(self, description):
        """
            Constructor method.
        :param description: Text description for this room
        """
        self.description = description
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
        # self.room_items.append(item)
    
        self.room_items[item.item_name] = item


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
