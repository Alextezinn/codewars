"""

Create a class Vector that has simple (3D) vector operators.

In your class, you should support the following operations, given Vector a and Vector b:

a + b # returns a new Vector that is the resultant of adding them
a - b # same, but with subtraction
a == b # returns true if they have the same magnitude and direction
a.cross(b) # returns a new Vector that is the cross product of a and b
a.dot(b) # returns a number that is the dot product of a and b
a.to_tuple() # returns a tuple representation of the vector.
str(a) # returns a string representation of the vector in the form "<a, b, c>"
a.magnitude # returns a number that is the magnitude (geometric length) of vector a.
a.x # gets x component
a.y # gets y component
a.z # gets z component
Vector([a,b,c]) # creates a new Vector from the supplied 3D array.
Vector(a,b,c) # same as above

"""
import math


class Vector:
    def __init__(self, *args):
        if len(args) == 1:
            self._x, self._y, self._z = args[0]

        else:
            self._x, self._y, self._z = args

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    @property
    def magnitude(self):
        return math.sqrt(self._x ** 2 + self._y ** 2 + self._z ** 2)

    def cross(self, vector):
        return Vector(self._y * vector._z - self._z * vector._y, self._z * vector._x - self._x * vector._z,
                      self._x * vector._y - self._y * vector._x)

    def dot(self, vector):
        return self._x * vector._x + self._y * vector._y + self._z * vector._z

    def to_tuple(self):
        return self._x, self._y, self._z

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y and self._z == other._z

    def __add__(self, vector):
        x = self._x + vector._x
        y = self._y + vector._y
        z = self._z + vector._z
        return Vector(x, y, z)

    def __sub__(self, vector):
        x = self._x - vector._x
        y = self._y - vector._y
        z = self._z - vector._z
        return Vector(x, y, z)

    def __str__(self):
        return f"<{self._x}, {self._y}, {self._z}>"