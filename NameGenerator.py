import random
import string
class NameGenerator:

    __namePrefix = ""

    # Instance attribute
    def __init__(self):
        self.__namePrefix = self.__generateName(10)

    def __generateName(self, length):
        # Define the character set to use
        characters = string.ascii_letters + string.digits

        # Generate the random string
        random_string = ''.join(random.choice(characters) for i in range(length))
        return random_string


    def get_name(self):
        return self.__namePrefix


