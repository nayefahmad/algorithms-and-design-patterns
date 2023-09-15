# # Decorator pattern in python

# ## References:

# - [Refactoring Guru article on Decorator pattern](https://refactoring.guru/design-patterns/decorator)  # noqa
# - [The Composition Over Inheritance Principle](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-if-statements)  # noqa

# ## Summary of pattern

# Decorator is a structural design pattern that lets you attach new behaviors to
# objects by placing these objects inside special wrapper objects that contain the
# behaviors.


class Component:
    """
    The base Component interface defines operations that can be altered by
    decorators.
    """

    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.
    """

    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """
        The Decorator delegates all work to the wrapped component.

        Side note: this is a pretty standard way to use the @property decorator. The
        result of this use is that we can access `component` as an attribute (like
        `a.component)` instead of like a function (like `a.component()). This can be
        useful in combination with a "setter" decorator like this:

        ```
        @component.setter
        def component(self, value):
            # validate that value is acceptable
            self._component = value
        ```

        With the setter implemented, we could dynamically catch invalid assignment.

        Another reason to use @propery is for derived/computed attributes in
        dataclasess, where those values
        are computed based on other attributes. Example:

        ```
        class Rectangle:
            def __init__(self, width, height):
                self.width = width
                self.height = height

            @property
            def area(self):
                return self.width * self.height

        # Usage:
        rect = Rectangle(4, 5)
        print(rect.area)  # Output: 20
        ```

        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """

    def operation(self) -> str:
        """
        Decorators may call parent implementation of the operation, instead of
        calling the wrapped object directly. This approach simplifies extension
        of decorator classes.
        """
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):
    """
    Decorators can execute their behavior either before or after the call to a
    wrapped object.
    """

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def client_code(component: Component) -> None:
    """
    The client code works with all objects using the Component interface. This
    way it can stay independent of the concrete classes of components it works
    with.
    """

    # ...

    print(f"RESULT: {component.operation()}", end="")

    # ...


if __name__ == "__main__":
    # This way the client code can support both simple components...
    simple = ConcreteComponent()
    print("1. Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as decorated ones.

    # Note how decorators can wrap not only simple components but the other
    # decorators as well.
    decorator1 = ConcreteDecoratorA(simple)
    print("2. Client: Now I've got a decorated component:")
    client_code(decorator1)
    decorator1.operation()
    print("\n")

    # You can even nest decorators:
    decorator2 = ConcreteDecoratorB(decorator1)
    print("3. Client: Now I've got a doubly decorated component:")
    client_code(decorator2)
    decorator2.operation()
    print("\n")

    # reversing the order of operations:
    wrapped01 = ConcreteDecoratorB(simple)
    wrapped02 = ConcreteDecoratorA(wrapped01)
    print("4. Client: Now I'll reverse the order of nesting the decorators:")
    client_code(wrapped02)
    wrapped02.operation()
