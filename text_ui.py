"""
A simple text based User Interface (UI) for the Adventure World game.
"""


import textwrap

class TextUI:

    def __init__(self):
        # Nothing to do...
        pass

    def get_command(self):
        """
            Fetches a command from the console.
        :return: a 2-tuple of the form (command_word, second_word)
        """
        word1 = None
        word2 = None
        print('> ', end='')
        input_line = input()
        if input_line != "":
            all_words = input_line.split()
            word1 = all_words[0]
            if len(all_words) > 1:
                word2 = all_words[1]
            else:
                word2 = None
            # Just ignore any other words
        return (word1, word2)
    
    def print_welcome(self):
        """
            Displays a welcome message.
        :return: None
        """
        # self.print_to_textUI("You are lost. You are alone. You wander")
        # self.print_to_textUI("around the deserted complex.")
        # self.print_to_textUI("")
        self.print_to_textUI("""
        
        In the eerie silence of a long-forgotten research complex, shadows danced menacingly 
        across abandoned hallways. A lone survivor of an ill-fated expedition, found 
        himself trapped within its labyrinthine corridors. As he navigated through the dimly 
        lit chambers, flickering lights revealed cryptic symbols etched on the walls, hinting 
        at an otherworldly experiment gone awry. 
        
        The air was thick with an unsettling tension,
        and distant echoes of unseen horrors amplified the sense of isolation. Your only 
        companions are the haunting memories of your colleagues and the lingering uncertainty 
        of the complex's malevolent secrets. Unraveling the mystery became not just a quest for 
        survival, but a descent into the unknown depths of a forsaken realm.

        You do not want to perish here, alone and maybe part of an perverse experiment so you move
        and look your way out of the small room.
                                """)

    def show_posible_movements(self):
        """
            Show the possible movements that the player can do
        """
        return ['north, south, west, east']

    def guess_puzzle_info(self):
        """
            Show the information related to guess the number puzzle
            and some game context
        """
        self.print_to_textUI("""

        Let's play a little guess game, is simple you just have to type the number of years you are
        going to spend here trying to escape to finally be part of our experimets...

        How to play:
        Type a number from 1 to 30, you are going to know if your guess is too high or too low.
        When solve the puzzle, an item will be added to your backpack.
        Be sure that you have enough space!
                            """)
        
    def mini_game_info(self):
        """
            Show the information related to mini_game in laundry room
            and some game context
        """
        self.print_to_textUI("""

        You have come a long way in escaping from our experiment complex, of course it would be unfair 
        to a little mouse like you not to give you the slightest chance to escape. Therefore, if you 
        solve the following mini_game you will have more information to find a way out, although you 
        know you will never find it.
        
        If you manage to solve the game little mouse, the dining_room door will open, good luck.

        How to play:
        Order the figures in the correct order, the answer is random so try as many combinations as you
        can. The figures are: triangle, square, circle. Please type the exact name of each figure, however
        you have all the time you need and wrong answers won't affect your escape!
                            """)

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: None
        """
        return ['help', 'go', 'current room', 'explore', 'pick', 'items', 'use', 'remove','quit']

    def print_lines(self):
        """
            Print some lines to make easier to understand the text and commands
        """
        self.print_to_textUI("---------------------------------------------------------")

    def print_help(self):
        """
            Display some useful help text.
        :return: None
        """
        self.print_to_textUI(f'Your command words are: {self.show_command_words()}.')
        self.print_to_textUI("To move through the map use the command 'go' + 'direction you want to go'")
        self.print_to_textUI("The 'current room' commmand give your current position")
        self.print_to_textUI("The 'explore' command shows the items that you can pick in that room")
        self.print_to_textUI("To pick an item in the room use command 'pick' + 'item you want to pick'")
        self.print_to_textUI("To use an item, type command 'use' + 'item you want to use'")
        self.print_to_textUI("To remove an item from backpack, type command 'remove' + 'item you want to remove'")
        self.print_to_textUI("Use 'quit' command to finish the game")

        # ['help', 'go', 'current room', 'explore', 'pick', 'items', 'use', 'remove','quit']

    def print_to_textUI(self, text):
        """
            Displays text to the console.
        :param text: Text to be displayed
        :return: None
        """
        return print(text)
