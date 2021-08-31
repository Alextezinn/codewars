"""

How many times we create a python class and in the init method we just write:

self.name1 = name1
self.name2 = name2
.....

for all arguments.....

How boring!!!!

Your task here is to implement a metaclass that let this instantiation be done automatically.
But let's see an example:

class Person(metaclass=LazyInit):
  def __init__(self, name, age): pass

When we create a Person object like:

a_person = Person('John', 25)

The expected behavior will be:

print(a_person.name) # this will print John
print(a_person.age)  # this will print 25

Obviously the number of arguments might be different from class to class.

Don't worry about **kwargs you will never be given keyword arguments in this kata!!!

A little hint: a decorator could help you out doing the job!!!

"""
# the metaclass to be used
class LazyInit(type):
    def __call__(self, *args):
        """ Вызов класса создает новый объект. """
        # Перво-наперво создадим сам объект...
        obj = type.__call__(self, *args)

        # и добавим ему переданные в вызове аргументы в качестве атрибутов.
        for field, value in zip(obj.__init__.__code__.co_varnames[1:], args):
            setattr(obj, field, value)

        # вернем готовый объект
        return obj
