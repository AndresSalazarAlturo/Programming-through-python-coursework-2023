"""
This class is the main class of the "Adventure World" application.
'Adventure World' is a very simple, text based adventure game. Users can walk
around some scenery. That's all. It should really be extended to make it more
interesting!

To play this game, create an instance of this class and call the "play" method.

This main class creates and initialises all the others: it creates all rooms,
creates the parser and starts the game. It also evaluates and executes the
commands that the parser returns.

This game is adapted from the 'World of Zuul' by Michael Kolling and 
David J. Barnes. The original was written in Java and has been simplified and
converted to Python by Kingsley Sage.
"""


from room import Room
from text_ui import TextUI
from items import Item
from backpack import Backpack

class Game:

    def __init__(self):
        """
        Initialises the game.
        """
        ##Dictionary with all rooms, key as string name and value as object
        self.game_rooms = {}
        ##Set up all rooms and objects
        self.create_rooms()
        ##Initial position
        self.current_room = self.cleaning_room
        self.textUI = TextUI()

    def create_rooms(self):
        """
            Sets up all room assets.
        :return: None
        """
        #########################################
        ######Now create the room objects########
        #########################################

        ##Initialise all the rooms in the map
        self.first_room = Room("your Initial location")

        ##Intialize corridor1
        self.corridor1 = Room("in a corridor1")

        ##Rooms option to corridor1
        self.cleaning_room = Room("in the cleaning room")
        self.security_room = Room("in the security room", password='1234')

        ##Initialize corridor2
        self.corridor2 = Room("in a corridor2", locked="card")

        ##Rooms option to corridor2
        self.lab = Room("in a computing lab", password='4321')
        self.office = Room("in the computing admin office", locked="card2")
        self.kitchen = Room("in the kitchen")

        ##Kitchen options
        self.stairs = Room("You are in the stairs")
        self.garden = Room("in the garden")
        self.dining_room = Room("in the dining room")

        ##Stairs options
        self.basement = Room("You are in the basement")

        ##Basement options
        self.laundry_room = Room("You are in the laundry room")
        self.storage = Room("Ypu are in the storage")

        #########################################
        ####Now create the exits for each room###
        #########################################

        ##First room posibilities
        """Empty room, nothing to look for"""
        self.first_room.set_exit("north", self.corridor1)

        ##Corridor1 posibilities
        self.corridor1.set_exit("west", self.cleaning_room)
        self.corridor1.set_exit("east", self.security_room)
        self.corridor1.set_exit("north", self.corridor2)
        self.corridor1.set_exit("south", self.first_room)

        ##Cleaning room posibilites
        """Could find a hint to solve a puzzle"""
        self.cleaning_room.set_exit("east", self.corridor1)

        ##Security room posibilities
        """Could find the key to go into the kitchen"""
        self.security_room.set_exit("west", self.corridor1)

        ##Corridor2 posibilities
        self.corridor2.set_exit("west", self.lab)
        self.corridor2.set_exit("east", self.office)
        self.corridor2.set_exit("north", self.kitchen)
        self.corridor2.set_exit("south", self.corridor1)

        ##Lab posibilities
        self.lab.set_exit("east", self.corridor2)
        
        ##Office posibilities
        self.office.set_exit("west", self.corridor2)

        ##Kitchen posibilities
        self.kitchen.set_exit("west", self.garden)
        self.kitchen.set_exit("east", self.dining_room)
        self.kitchen.set_exit("north", self.stairs)
        self.kitchen.set_exit("south", self.corridor2)

        ##stairs posibilities - Change this options
        self.stairs.set_exit("north", self.basement)
        self.stairs.set_exit("south", self.kitchen)

        ##Garden posibilities
        self.garden.set_exit("east", self.kitchen)

        ##Dining room posibilities
        self.dining_room.set_exit("west", self.kitchen)

        ##Basement posibilities
        self.basement.set_exit("west", self.storage)
        self.basement.set_exit("east", self.laundry_room)

        ##Storage posibilities
        self.storage.set_exit("east", self.basement)

        ##Laundry room posibilities
        self.laundry_room.set_exit("west", self.basement)

        ###############################
        #####Initialize the objects####
        ###############################

        # Create items for cleaning room
        self.card = Item("card", "could open a door")
        self.code = Item("code", 1234)
        self.stone = Item("stone", "allow teleport")

        ## Create items for security room
        self.card2 = Item("card2", "could open another door")

        # Add items to cleaning room
        self.cleaning_room.add_item_to_room(self.card)
        self.cleaning_room.add_item_to_room(self.code)
        self.cleaning_room.add_item_to_room(self.stone)

        # Add items to security room
        self.security_room.add_item_to_room(self.card2)

        ################################
        #####Initialize the backpack####
        ################################

        ##Create the backpack
        self.backpack = Backpack(4)

        ##Create a dictionary with all positions
        self.game_rooms = {"first_room":self.first_room, "corridor1":self.corridor1, "cleaning_room":self.cleaning_room,"security_room":self.security_room,
                           "corridor2":self.corridor2, "computing_lab":self.lab, "office":self.office, "kitchen":self.kitchen,
                           "stairs":self.stairs, "garden":self.garden, "dining_room":self.dining_room}

    def play(self):
        """
            The main play loop.
        :return: None
        """

        self.textUI.print_welcome()
        finished = False
        while not finished:
            self.textUI.print_to_textUI(f'command words: {self.textUI.show_command_words()}')
            self.textUI.print_to_textUI(f'possible movements: {self.textUI.show_posible_movements()}')
            command = self.textUI.get_command()  # Returns a 2-tuple
            finished = self.process_command(command)
        print("Thank you for playing!")

    def process_command(self, command):
        """
            Process a command from the TextUI.
        :param command: a 2-tuple of the form (command_word, second_word)
        :return: True if the game has been quit, False otherwise
        """
        command_word, second_word = command
        if command_word != None:
            command_word = command_word.upper()
            if second_word == "room":
                second_word = second_word.upper()

        want_to_quit = False
        if command_word == "HELP":
            ##Show useful information about the game and commands
            self.textUI.print_help()
        elif command_word == "GO":
            ##Direction is the second word
            self.do_go_command(second_word)
        elif command_word == "CURRENT" and second_word == "ROOM":
            ##Display current room info
            self.textUI.print_to_textUI(self.current_room.get_short_description())
        elif command_word == "EXPLORE":
            ##Show the available items in the room
            self.textUI.print_to_textUI(self.current_room.get_room_items())
        elif command_word == "PICK":
            ##Item to pick is the second word
            self.do_pick_command(second_word)
        elif command_word == 'ITEMS':
            self.textUI.print_to_textUI(self.backpack.show_all_items())
        elif command_word == "USE":
            # # check player has item
            # if 
            # # check the room can use the item
            # pass
            self.do_use_command(second_word)
        elif command_word == 'REMOVE':
            ##Item to delete is second word
            self.do_remove_command(second_word)
        elif command_word == "QUIT":
            ##Close the game
            want_to_quit = True
        else:
            # Unknown command...
            self.textUI.print_to_textUI("Don't know what you mean.")

        return want_to_quit
    
    def do_use_command(self, second_word):
        """
            Performs the USE command. Now performs the teleport with the 'stone' object
            :param second_word: the item the player wants to remove from backpack
            :return: None
        """

        if second_word == None:
            # Missing second word...
            self.textUI.print_to_textUI("use what item?")
            return
        
        room_response = self.current_room.allow_teleport(self.backpack, self.game_rooms)
        if room_response == False:
            self.textUI.print_to_textUI("You do not have the stone to teleport")
        elif room_response == None:
            return
        else:
            self.current_room = room_response
            self.textUI.print_to_textUI(self.current_room.get_long_description())

    def do_remove_command(self, second_word):
        """
            Performs the REMOVE command.
        :param second_word: the item the player wants to remove from backpack
        :return: None
        """

        if second_word == None:
            # Missing second word...
            self.textUI.print_to_textUI("Remove what item?")
            return
        
        self.backpack.remove_item(second_word)
    
    def do_pick_command(self, second_word):
        """
            Performs the PICK command.
        :param second_word: the item the player wants to add to backpack
        :return: None
        """
        if second_word == None:
            # Missing second word...
            self.textUI.print_to_textUI("Pick what item?")
            return
        
        if self.backpack.check_item(second_word):
            self.textUI.print_to_textUI("Item already in the backpack")
        else:
            try:
                self.backpack.add_item(self.current_room.room_items[second_word])
            except KeyError:
                print("Item not in the room")

    def do_go_command(self, second_word):
        """
            Performs the GO command.
        :param second_word: the direction the player wishes to travel in
        :return: None
        """
        if second_word == None:
            # Missing second word...
            self.textUI.print_to_textUI("Go where?")
            return

        ## get_exit return the room object
        next_room = self.current_room.get_exit(second_word)
        if next_room == None:
            self.textUI.print_to_textUI("There is no door!")

        else:
            ## Check if the room has password
            if next_room.password is not None:
                self.textUI.print_to_textUI("Type the password")
                password, second_word = self.textUI.get_command()
                if next_room.can_enter(self.backpack, password=password):
                    ##Enter the room
                    self.current_room = next_room
                    self.textUI.print_to_textUI(self.current_room.get_long_description())
                    return
                else:
                    self.textUI.print_to_textUI(self.current_room.get_long_description())
                    return
            
            ## Check if the room is locked
            if next_room.locked is not None:
                ## Go inside the room if does not require card, password and it was typed properly
                if next_room.can_enter(self.backpack):
                    self.current_room = next_room
                    self.textUI.print_to_textUI(self.current_room.get_long_description())
                    return
                else:
                ## If the card is not in the backpack, stay in the current room, not access allowed
                    self.textUI.print_to_textUI(self.current_room.get_long_description())
                    return
            ## If the rooms does not have key or password just go in
            self.current_room = next_room
            self.textUI.print_to_textUI(self.current_room.get_long_description())

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
