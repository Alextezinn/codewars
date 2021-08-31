"""

Description
Your task is to create a class Function, that will be provided with 2 arguments - f &
df - representing a function and its derivative. You should be able to do function algebra with this
class, i.e. they can be added, subtracted, multiplied, divided and composed to give another
Function object with a valid function and a derivative. When the function is called, it must have
a optional grad argument. The functions will be called with only one argument. If then function is
called without the grad argument, return the value of the function, and if grad = True, return the
value of its derivative.

The class should behave like given below:

square = Function(lambda x: x**2, lambda x: 2*x)
identity = Function(lambda x: x, lambda x: 1)
square(1) # => 1
square(1, grad = True) # => 2

The class should also exibit these behaviours:

f = square + identity
f(1) # => 2
f(1, grad = True) # => 3

g = square - identity
g(1) # => 0
g(1, grad = True) # => 1

h = square * identity
h(1) # => 1
h(1, grad = True) # => 3

i = square / identity
i(1) # => 1
i(1, grad = True) # => 1

j = square @ identity # f @ g means f(g(x))
j(1) # => 1
j(1, grad = True) # => 2
"""
class Function:
    def __init__(self, f, df):
        self._f = f
        self._df = df

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, value):
        self._f = value

    @property
    def df(self):
        return self._df

    @df.setter
    def df(self, value):
        self._df = value

    def __call__(self, v, grad=False):
        return self._df(v) if grad else self._f(v)

    def __eq__(self, other):
        return self._f == other._f and self._df == other._df

    def __add__(self, other):
        f = lambda v: self._f(v) + other._f(v)
        df = lambda v: self._df(v) + other._df(v)
        return Function(f, df)

    def __sub__(self, other):
        f = lambda v: self._f(v) - other._f(v)
        df = lambda v: self._df(v) - other._df(v)
        return Function(f, df)

    def __mul__(self, other):
        f = lambda v: self._f(v) * other._f(v)
        df = lambda v: self._df(v) * other._f(v) + other._df(v) * self._f(v)
        return Function(f, df)

    def __truediv__(self, other):
        f = lambda v: self._f(v) / other._f(v)
        df = lambda v: (self._df(v) * other._f(v) - other._df(v) * self._f(v)) / other._f(v) ** 2
        return Function(f, df)

    def __matmul__(self, other):
        f = lambda v: self._f(other._f(v))
        df = lambda v: self._df(other._f(v)) * other._df(v)
        return Function(f, df)