# # Refactoring complex if-else blocks

# References:
# - [Sunny Sun on Medium](https://betterprogramming.pub/4-simple-and-effective-ways-to-avoid-too-many-ifs-with-typescript-89937c0f9a99)  # noqa
# - [Jan on Medium](https://janalmazora.medium.com/how-to-prevent-using-if-else-statements-in-your-code-7e05e43afde)  # noqa


# ## Set up tests:
def run_test_cases(function):
    test_cases = {
        1: ("200", None),
        2: ("200", ""),
        3: ("404", "error 200"),
        4: ("404", None),
    }

    expected_outputs = {
        1: "success",
        2: "success",
        3: "error 200",
        4: "unexpected error",
    }

    for test_case in range(1, 5):
        print(f"Running test case: {test_case} on function {function.__name__}")
        assert function(*test_cases[test_case]) == expected_outputs[test_case]
    print("All tests passed")


# ## Initial state of function:

# Notes:

# 1. We have to keep track of how the `status` variable changes throughout the function.
#   It could be overriden in non-intuitive ways after being initially assigned to.


def complex_if_else(response_status, response_error):
    if response_status == "200":
        status = "success"
    else:
        if response_error:
            status = f"{response_error}"
        else:
            status = "unexpected error"
    return status


run_test_cases(complex_if_else)


# ## Solution 1: Guard and early return


def guard(response_status, response_error):
    if response_status != "200":
        if response_error is not None:
            return f"{response_error}"
        else:
            return "unexpected error"
    status = "success"
    return status


run_test_cases(guard)
