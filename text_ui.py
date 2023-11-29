"""
A simple text based User Interface (UI) for the Adventure World game.
"""

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
        self.print_to_textUI("You are lost. You are alone. You wander")
        self.print_to_textUI("around the deserted complex.")
        self.print_to_textUI("")

    def show_posible_movements(self):
        """
            Show the possible movements that the player can do
        """
        return ['north, south, west, east']

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: None
        """
        return ['help', 'go', 'current room', 'explore', 'pick', 'items', 'use', 'remove','quit']
        
    def objetives(self):
        """
            Show the current objetive and change when its done to the next one
        """
        
        pass

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
