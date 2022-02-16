import random 


class Insect:

    #The __init__ method initializes the 
    #attributes with wings and legs

    def __init__(self, wings, legs):
        self.legs = legs
        self.wings = wings
        self.flight = 0

    def flight_length(self):
        self.flight = random.randint(1, 10)

    #Method to determine the length of flight 
    def get_flight(self):
        return self.flight