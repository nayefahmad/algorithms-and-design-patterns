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
