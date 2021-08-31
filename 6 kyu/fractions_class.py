"""

You are provided with a skeleton of the class 'Fraction', which accepts two arguments
(numerator, denominator).

EXAMPLE:
    fraction1 = Fraction(4, 5)

Your task is to make this class string representable, and addable while keeping the result
in the minimum representation possible.

EXAMPLE:
    print (fraction1 + Fraction(1, 8))
    outputs: 37/40

"""


class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def __str__(self):
        return str(self.top) + "/" + str(self.bottom)

    def __add__(self, fraction):
        new_top = self.top * fraction.bottom + self.bottom * fraction.top
        new_bottom = self.bottom * fraction.bottom
        common = Fraction.gcd(new_top, new_bottom)
        return Fraction(new_top // common, new_bottom // common)

    @staticmethod
    def gcd(a, b):
        while a % b != 0:
            m, n = a, b
            a, b = n, m % n

        return b