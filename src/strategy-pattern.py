# Strategy pattern in Python

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


# ## Classes used

# We will use a `Context` class, a `Strategy` interface, and several specific
# implementations of the interface.


# ### Libraries

from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List) -> List:
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def do_some_business_logic(self) -> List:
        result = self._strategy.do_algorithm(["a", "b", "c"])
        return result


if __name__ == "__main__":
    context = Context(ConcreteStrategyA)
