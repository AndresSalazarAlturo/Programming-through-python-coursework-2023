"""
    Here will be all the custome exceptions
"""

class NotInBackpackError(Exception):
    def __init__(self, item, message):
        print(f'{item} {message}')

class FullBackpackError(Exception):
    def __init__(self, capacity, message):
        print(f'{message}, you backpack capacity is {capacity}')

class WrongPassword(Exception):
    def __init__(self, message):
        print(f'{message}')