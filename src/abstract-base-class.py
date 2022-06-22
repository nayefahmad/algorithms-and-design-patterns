# # Abstract Base Classes and the abstractmethod decorator

# ## Overview

# If you define a class named, say BaseClass that subclasses ABC, and has methods that
# are prepended with the decorator @abstractmethod, then:
# - You can't instantiate BaseClass.
# - You can subclass it in, e.g. ChildClass
# - However, you can't instantiate ChildClass unless it overrides all the
# @abstractmethod methods in BaseClass

# Upshot: BaseClass is a pattern/template that you define that all child classes must
# follow

# In this script, we demonstrate that
#
# 1. The class `BaseClassWithoutAbstractMethod` can be instantiated and
# subclassed, and the subclass can be instantiated even without overriding the `fit`
# method. This is **not** how abstract classes are intended to be used.
# 2. The class `BaseClass`, which has a method that is decorated with `@abstractmethod`,
# can't be instantiated on its own. Also, any child class can't be instantiated unless
# it overrides the methods decorated with `@abstractmethod`


from abc import ABC, abstractmethod


class BaseClassWithoutAbstractMethod(ABC):
    def __init__(self):
        pass

    def fit(self):
        print(f"You called fit() on: {self}")


b1 = BaseClassWithoutAbstractMethod()
b1.fit()


class ChildClassWithoutAbstractMethod(BaseClassWithoutAbstractMethod):
    def __init__(self):
        super(ChildClassWithoutAbstractMethod, self).__init__()

    def fit(self):
        print(f"You called fit() on: {self}")


c1 = ChildClassWithoutAbstractMethod()
c1.fit()


# ## Using ABCs as intended:


class BaseClass(ABC):
    def __init__(self):
        pass

    @abstractmethod  # this is the only difference between BaseClassWithoutAbstractMethod and BaseClass  # noqa
    def fit(self):
        print(f"You called fit() on: {self}")


try:
    b2 = BaseClass()  # BaseClass can't be instantiated
    b2.fit()
except TypeError as e:
    print(f"Failed! Error message: \nTypeError: {e}")


class ChildClass(BaseClass):
    def __init__(self):
        super(ChildClass, self).__init__()


# ChildClass can't be instantiated because it failed to override the fit method of
# parent ABC, BaseClass2
try:
    c2 = ChildClass()  # error
    c2.fit()
except TypeError as e:
    print(f"Failed! Error message: \nTypeError: {e}")


# Finally, here's a child class that works as intended:


class ChildClassWithFitOverride(BaseClass):
    def __init__(self):
        super(ChildClassWithFitOverride, self).__init__()

    def fit(self):
        print(f"You called fit() on: {self}")


c3 = ChildClassWithFitOverride()
c3.fit()
