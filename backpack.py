from my_exceptions import NotInBackpackError, FullBackpackError

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
                # self.contents.append(item)
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
        # finally:
        #     print('Carrying on...')

    def show_all_items(self):
        """
            Print all items in the backpack
        """
        print("Your items are:\n")
        for item in self.contents:
            print(f'{item}')

    def check_item(self, item):
        """Returns True if item is in backpack, False otherwise."""
        return item in self.contents

