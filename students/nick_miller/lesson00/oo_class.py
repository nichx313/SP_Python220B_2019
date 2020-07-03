"""
simple oo example
"""


class Pet:
    """ This class defines Pet, which is an animal kept by a human for domestic purposes" """
    def __init__(self, name):
        self.name = name
        self.hello = "Blub"

    def speak(self):
        """ sample - maybe lots of code in this """
        return self.hello

    def swim(self):
        return "Splash"


mypet = Pet("Goldie")  # i am an object: an instance of the class Pet

print(mypet.name)
print(mypet.speak())
print(mypet.swim())
import sphinx
import pytest
