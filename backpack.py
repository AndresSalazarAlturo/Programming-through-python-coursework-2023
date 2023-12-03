import time
import random
import os
from src.my_exceptions import NotInBackpackError, FullBackpackError

class Backpack:
    """
    A class to allow us to pickup and put down items...
    Backpack is limited to number of items set by capacity.
    This example incorporates a user defined exception.
    """

    def __init__(self, capacity):
        self.contents = {}          ##Dictionaty of items with their description as a value
        self.capacity = capacity    ##Backpack capacity

    def add_item(self, item):
        """Adds an item to our backpack."""
        try:
            if len(self.contents) < self.capacity:
                self.contents[item.item_name] = item
                return True
            else:
                raise FullBackpackError(self.capacity, 'Your backpack is full')
        except FullBackpackError:
            print("The back pack is full")
            return False

    def remove_item(self, item):
        """Removes an item from our backpack."""
        try:
            if item not in self.contents:
                raise NotInBackpackError(item, 'is not in the backpack.')
            self.contents.pop(item)
            return True
        except NotInBackpackError:
            print("Check your items with 'items' command and delete one of them if you want")
            return False
        # finally:
        #     print('Carrying on...')

    def increase_backpack_capacity(self, item):
        """
            Increase the backpack capacity
            :param backpack: Backpack object
        """
        if item in self.contents:
            increase_value = self.contents[item]
            self.capacity += increase_value.feature
            print(f"The new backpack capacity is {self.capacity}")
            return True
        else:
            return False
        
    def process_operation_game(self, dining_room_item):
        """
            Process the operation game, create the random numbers and the timer
            :param hidden_items: Dictionary with the current room hidden objects
            :return: True if solve the questions in time, False if not
        """
        cnt = 0 
        timeout = 60                    ## Time to answer the questions
        start_time = time.time()        ## Set the start time to compare it with the current time
        number_of_operations = 2

        quit_operation_game = True
        print("Solve 2 questions to get the object")
        print("Type '000' to quit the game")

        dining_room_lock = dining_room_item["dining_room"]

        while quit_operation_game:

            num1 = random.randint(-20, 20)
            num2 = random.randint(-20, 20)
            correct_answer = num1 + num2

            print(f"What is the sum of {num1} and {num2}?")

            try:
                user_answer = int(input("Your answer: "))
            except ValueError:
                print("Invalid input. Please enter a valid number")
                continue

            if time.time() - start_time > timeout:
                print("Time is up! You took too long to answer")
                quit_operation_game = False

            if user_answer == correct_answer:
                cnt += 1
                print("Correct! Your score is now:", cnt)
                if cnt == number_of_operations:
                    print("You answer correctly all the questions!")
                    ##Open the dining_room door
                    dining_room_lock.locked = False
                    print("The dining_room door is now open")
                    quit_operation_game = False

            elif user_answer == 000:
                quit_operation_game = False

            else:
                print("Wrong answer. Try again.")

        print("Final score: ", cnt)

    def process_hangman_game(self, hidden_items):
        """
            Process the hangman game.
            :param hidden_items: Dictionary with the current room hidden objects
            :return: True if solve the questions in time, False if not
        """

        filepath="./src/data.txt"

        with open(filepath, "r", encoding="utf-8") as f:
        
            words = []
            for word in f:
                words.append(word.strip().upper())

        my_word = random.choice(words)
        my_word_spaces = [letter for letter in my_word]
        my_word_spaces_underscores = ["_"] * len(my_word)
        word_dict = {}

        for key, value in enumerate(my_word):
            if not word_dict.get(value):
                word_dict[value] = []
            word_dict[value].append(key)

        while (True):
            os.system("cls")
            print("¡Guess the word!")

            print(my_word)

            for under_score in my_word_spaces_underscores:
                print(under_score + " ", end = "")
            print("\n")
            
            try:
                letter = input("Try any letter \n").strip().upper()
            except ValueError:
                print("Just letter please")

            if letter in my_word_spaces:
                for key in word_dict[letter]:
                    my_word_spaces_underscores[key] = letter
            elif letter == my_word:
                os.system("cls")
                print("¡You won! The word was ", my_word)
                print("You answer correctly all the questions!")
                self.add_item(hidden_items["key"])
                print("A new item has been added to your backpack!")
                break

            elif letter == "BACK":
                break

            if "_" not in my_word_spaces_underscores:
                os.system("cls") 
                print("¡You won! The word was ", my_word)
                print("You answer correctly all the questions!")
                self.add_item(hidden_items["key"])
                print("A new item has been added to your backpack!")
                break

    def solve_puzzle(self, guess, hidden_items):
        """
            Create a basic guess the number puzzle, the user knows if the guess
            is too high or too low
            :param guess: user guess
            :param backpack: Players backpack - backpack object
            :return: True when the user guess the number
        """
        random.seed(20)
        num = random.randint(1, 10)

        if guess == num:
            print("congratulations! you won!")
            self.add_item(hidden_items["document1"])
            print("A new item has been added to your backpack!")
            print("Check it to know where to look the key!")
            return True

        elif guess > num:
            print("Your guess is too high")

        elif guess < num:
            print("Your guess is too low")

        else:
            print("nope, sorry. try again!")

    def process_mini_game(self, hidden_items):
        """
            Process the mini_game - The game consist in introduce in correct order the figures to
            unlock the dining room
            :param game_rooms: Get the game rooms and access de dining_room object
            :return: True or False depending if solve the mini_game
        """
        list_of_items = ["square", "triangle", "circle"]

        ##shuffle the list order randomly
        random.seed(10)
        random.shuffle(list_of_items)
        print(list_of_items, "--> solution")

        user_input = []
        for i in range(1, len(list_of_items) + 1):
            user_input.append(input(f"Type the object {i}: "))
        if list_of_items == user_input:
            print("you solve the puzzle")
            ##Add the laundry_password item to backpack
            self.add_item(hidden_items["laundry_password"])
            return False
        else:
            print("Try again")
            return True

    def show_puzzle_items(self):
        """
            Show the items that are puzzles
        """
        pass

    def get_number_of_items(self):
        """
            Return the number of items in the backpack
        """
        all_items = list(self.contents.keys())
        return len(all_items)

    def show_all_items(self):
        """
            Print all items in the backpack
        """
        print("Your items are:\n")
        for item, feature in self.contents.items():
            print(f'{item} --> description: {feature.feature}')

    def check_item(self, item):
        """Returns True if item is in backpack, False otherwise."""
        return item in self.contents

