"""Write a simple Promo class. Its constructor receives a name str and expires datetime. Add a property to called
expired which returns a boolean. Checkout the tests and datetime. Have fun!"""

from datetime import datetime

NOW = datetime.now()

class Promo:

    #initial function using dunder method
    def __init__(self, name, expired):
        self.name = name
        self._expired = expired #the underscore denotes the property

    @property
    def expired(self):
        if datetime.now() > self._expired: #compares current datetime with the the called attribute from the above dunder
            return True
        else:
            return False