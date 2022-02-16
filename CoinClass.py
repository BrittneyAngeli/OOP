import random

# The Coin class simulates a coin that can
# be flipped.

class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self):
        self.sideup = 'Heads'                       #sideup is an attribute name (chosen by user)

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.
                                                    #toss method is a get (mutated) method since it is "mutating" or changing 
    def toss(self):                                 #self parameter to refer to itself 
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    # The get_sideup method returns the value      #an accesssor methods - you can access methods 
    # referenced by sideup.

    def get_sideup(self):
            return self.sideup
