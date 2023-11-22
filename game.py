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
        self.create_rooms()
        ##Initial position
        self.current_room = self.first_room
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
        self.security_room = Room("in the security room")

        ##Initialize corridor2
        self.corridor2 = Room("in a corridor2")

        ##Rooms option to corridor2
        self.lab = Room("in a computing lab")
        self.office = Room("in the computing admin office")
        self.kitchen = Room("in the kitchen")

        ##Kitchen options
        self.outside = Room("You are outside")
        self.garden = Room("in the garden")
        self.dining_room = Room("in the dining room")

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
        self.kitchen.set_exit("north", self.outside)
        self.kitchen.set_exit("south", self.corridor2)

        ##Outside posibilities - Change this options
        self.outside.set_exit("south", self.kitchen)

        ##Garden posibilities
        self.garden.set_exit("east", self.kitchen)

        ##Dining room posibilities
        self.dining_room.set_exit("west", self.kitchen)

        ###############################
        #####Initialize the objects####
        ###############################

        # Create items
        self.card = Item("card", "could open a locker")
        self.code = Item("code", 1234)
        self.document = Item("document", "some important information to continue")

        ## Dictionary of all items
        

        # Add items to rooms
        self.cleaning_room.add_item_to_room(self.card)
        self.cleaning_room.add_item_to_room(self.code)
        self.cleaning_room.add_item_to_room(self.document)

        ################################
        #####Initialize the backpack####
        ################################

        ##Create the backpack
        self.backpack = Backpack(1)

    def play(self):
        """
            The main play loop.
        :return: None
        """

        self.print_welcome()
        finished = False
        while not finished:
            self.textUI.print_to_textUI(f'command words: {self.show_command_words()}')
            self.textUI.print_to_textUI(f'possible movements: {self.show_posible_movements()}')
            command = self.textUI.get_command()  # Returns a 2-tuple
            finished = self.process_command(command)
        print("Thank you for playing!")

    def print_welcome(self):
        """
            Displays a welcome message.
        :return: None
        """
        self.textUI.print_to_textUI("You are lost. You are alone. You wander")
        self.textUI.print_to_textUI("around the deserted complex.")
        self.textUI.print_to_textUI("")
        # self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}')

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: None
        """
        return ['help', 'go', 'current room', 'explore', 'pick', 'items', 'use', 'remove','quit']
    
    def show_posible_movements(self):
        """
            Show the possible movements that the player can do
        """
        return ['north, south, west, east']

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
            self.print_help()
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
        # elif command_word == "USE":
        #     # check player has item
        #     if 
        #     # check the room can use the item
        #     pass
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

        next_room = self.current_room.get_exit(second_word)
        if next_room == None:
            self.textUI.print_to_textUI("There is no door!")
        else:
            self.current_room = next_room
            self.textUI.print_to_textUI(self.current_room.get_long_description())

    def print_help(self):
        """
            Display some useful help text.
        :return: None
        """
        self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}.')
        self.textUI.print_to_textUI("To move through the map use the command 'go' + 'direction you want to go'")
        self.textUI.print_to_textUI("The 'current room' commmand give your current position")
        self.textUI.print_to_textUI("The 'explore' command shows the items that you can pick in that room")
        self.textUI.print_to_textUI("To pick an item in the room use command 'pick' + 'item you want to pick'")
        self.textUI.print_to_textUI("To use an item, type command 'use' + 'item you want to use'")
        self.textUI.print_to_textUI("To remove an item from backpack, type command 'remove' + 'item you want to remove'")
        self.textUI.print_to_textUI("Use 'quit' command to finish the game")

        # ['help', 'go', 'current room', 'explore', 'pick', 'items', 'use', 'remove','quit']

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
