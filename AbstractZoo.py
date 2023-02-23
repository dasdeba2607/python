"""
https://blog.teclado.com/python-abc-abstract-base-classes/
variation 1
from abstractClassAnimal import Animal


class Lion(Animal):
    def feed(self):
        print("Feeding a lion with raw meat!")

class Panda(Animal):
    def feed(self):
        print("Feeding a panda with some tasty bamboo!")

class Snake(Animal):
    def feed(self):
        print("Feeding a snake with mice!")


The following code is ok but we need to be smart enough in reducing codes, lets introduce abstractClass
lo = Lion()
pa = Panda()
sn = Snake()
lo.feed()
pa.feed()
sn.feed()
"""

"""
variation 2
# The following is an example of using abstract class without abstractmethod

from abc import ABC

class Lion(ABC):  ## if we create child class of ABC, it will still work for example class Lion(ABC)

    def feed(self):
        print("Feeding a lion with raw meat!")

class Panda(ABC):

    def feed(self):
        print("Feeding a panda with some tasty bamboo!")

class Snake(ABC):

    def feed(self):
        print("Feeding a snake with mice!")

myzoo = [Lion(), Panda(), Snake()]

for r in myzoo:
    r.feed()
"""

# variation 3
from abc import ABC, abstractmethod


class zoo(ABC):
    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def do(self, action):
        pass


class Lion(zoo):

    def feed(self):
        print("Feeding a lion with raw meat!")

    def do(self, action, time):
        print("{} a Lion! @ {}".format(action, time))


class Panda(zoo):

    def feed(self):
        print("Feeding a panda with some tasty bamboo!")

    def do(self, action, time):
        print("{} a Panda ! @ {}".format(action, time))


class Snake(zoo):

    def feed(self):
        print("Feeding a snake with mice!")

    def do(self, action, time):
        print("{} a Snake! @ {}".format(action, time))


class human(zoo):

    def feed(self):
        print("I am human")


# h = human() ## this will return error as in human child class, all abstractmethods are not overridden
# h.feed()
try:
    print(issubclass(Snake, zoo))
    print(isinstance(Snake, zoo))
    a = zoo()  ## you can not initiate abstract class
except Exception as err:
    print(err)

myzoo = [Lion(), Panda(), Snake()]

for r in myzoo:
    r.feed()

for r in myzoo:
    r.do(action="Playing", time="10:10:10 GMT")

"""
# variation 4
import abc
from abc import ABC, abstractmethod

class R(ABC):
    def rk(self):
        print("Abstract Base Class")

class K(R):
    def rk(self):
        super().rk()
        print("subclass ")

# Driver code
r = K()
r.rk()
"""

"""
variation 5
from abc import ABC, abstractmethod

class parent(ABC):

    @abstractmethod
    def geeks(self):
        return "parent class"

class child(parent):

    @property
    def geeks(self):
        return "child class"

try:
    r =parent()
    print( r.geeks)
except Exception as err:
    print(err)

r = child()
print (r.geeks)
"""
