class Item:
    """
        This class create each item in the game and provide the features for each item
    """
    def __init__(self, item, feature, puzzle = None):
        self.item_name = item
        self.feature = feature
        self.puzzle = puzzle

    def get_item_description(self):
        """
            Print the item description
            :return: None
        """
        print(f"{self.item_name} - {self.feature}")