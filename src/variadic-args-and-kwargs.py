"""
# Patterns with variadic args and kwargs

References:
    - D. Beazly, Python Distilled, p102-106
"""


def fixed_args():
    print("done")


def variadic_args(*args):
    print(f"args: {args}")
    print(f"*args: {args}")
    print("done")


def fixed_and_variadic_args(first, *args):
    print(f"*args: {args}")
    print("done")


def fixed_and_variadic_kwargs(first, **kwargs):
    print(f"**kwargs: {kwargs}")
    print("done")


def wrapper_function(first, *args, **kwargs):
    fixed_and_variadic_args(first, *args)
    fixed_and_variadic_kwargs(first, **kwargs)


if __name__ == "__main__":
    fixed_args()
    try:
        fixed_args(1)
    except TypeError as e:
        print(f"{type(e).__name__}: {e}")

    variadic_args()

    # In both these cases, within the function, args are unpacked as tuple (1,2)
    variadic_args(1, 2)
    variadic_args(*[1, 2])

    try:
        fixed_and_variadic_args()
    except TypeError as e:
        print(f"{type(e).__name__}: {e}")
    fixed_and_variadic_args(1)
    fixed_and_variadic_args(1, 2, 3)

    wrapper_function(1)
    wrapper_function(1, 2)

    # correct way to pass variadic kwargs:
    wrapper_function(1, 2, third=3)

    # INCORRECT way to pass variadic kwargs:
    wrapper_function(1, 2, {"third": 3})
