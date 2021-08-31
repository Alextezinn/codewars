"""

Can a value be both True and False?

Define omnibool so that it returns True for the following:

omnibool == True and omnibool == False
"""
class SchrodingerBoolean():
    def __eq__(self, _):
        return True

omnibool = SchrodingerBoolean()