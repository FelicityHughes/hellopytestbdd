class HelloWorld:
    """A Simple Hello World Example"""

    def __init__(self):
        self.__name = None
        self.__salutation = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def print_greeting(self):
        return self.__salutation + " " + self.__name + "!"

    @property
    def salutation(self):
        return self.__salutation

    @salutation.setter
    def salutation(self, value):
        self.__salutation = value
