# # Strategy pattern in Python

# ## References:

# - [Refactoring Guru article on Strategy pattern](https://refactoring.guru/design-patterns/strategy)  # noqa
# - [Refactoring Guru code example in Python](https://refactoring.guru/design-patterns/strategy/python/example)  # noqa


# ## Summary of the pattern

# Strategy is a behavioral design pattern that turns a set of behaviors into objects
# and makes them interchangeable inside the original context object.

# The original object, called context, holds a reference to a strategy object and
# delegates it executing the behavior. In order to change the way the context performs
# its work, other objects may replace the currently linked strategy object with another
# one.

# To make this more intuitive, the context is a `Duck` class. We want our ducks to
# quack, but there are many different ways to quack. To allow for runtime changes in
# quack behaviour, we make a `QuackBehaviour` interface and concrete classes for each
# specific way to quack.

# Notice that we don't have to change the `Duck` class in order to change the behaviour
# of ducks. Thus we effectively separate parts of the program that change often
# (quack behaviours) from parts that don't change often (the Duck itself). This is a
# key principle behind most design patterns.


# ## Classes used

# We will use a `Duck` class, a `QuackBehaviour` interface, and several specific
# implementations of the interface.


# ### Libraries

from abc import ABC, abstractmethod
from typing import List


# Interface for behaviours


class QuackBehaviour(ABC):
    @abstractmethod
    def do_algorithm(self, data: List) -> List:
        pass


# Specific behaviours


class QuackNormal(QuackBehaviour):
    def do_algorithm(self, data: List) -> List:
        return data


class QuackReversed(QuackBehaviour):
    def do_algorithm(self, data: List) -> List:
        return list(reversed(sorted(data)))


class QuackLastAndFirst(QuackBehaviour):
    def do_algorithm(self, data: List) -> List:
        return [data[-1]] + [data[0]]


# Context class


class Duck:
    def __init__(self, strategy: QuackBehaviour = QuackNormal):
        self._strategy = strategy()

    def do_some_business_logic(self, data) -> List:
        result = self._strategy.do_algorithm(data)
        return result


# ## Demo
data = [1, 2, 3, 4, 5]

for duck_num, strategy in enumerate([QuackNormal, QuackLastAndFirst, QuackReversed]):
    print(f"Duck {duck_num}, Strategy = {strategy}")
    duck = Duck(strategy)
    result = duck.do_some_business_logic(data)
    print(f"result = {result}")
