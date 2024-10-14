# Create a class for an insect object. It should have 2 attributes – wings
# and legs. For now, the insect object has 2 wings and 4 legs. It should
# also have 1 method – to determine the length of flight. Length of flight
# should be a method that randomly assigns a number between 1 and 10
# miles. Create a python program that will create an instance of the
# insect class and print out how many miles the insect can fly.

import random

class Insect:

    def __init__(self,w,l,n):
        self.wings = w
        self.legs = l
        self.flight = 0
        self.name = n

    def calc_flight(self):
        self.flight = random.randint(1,10)

    def get_flight(self):
        return self.flight
    
    def get_name(self):
        return self.name