# # Refactoring complex if-else blocks

# References:
# - [Sunny Sun on Medium](https://betterprogramming.pub/4-simple-and-effective-ways-to-avoid-too-many-ifs-with-typescript-89937c0f9a99)  # noqa
# - [Jan on Medium](https://janalmazora.medium.com/how-to-prevent-using-if-else-statements-in-your-code-7e05e43afde)  # noqa

# ## Initial state:

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


test_cases = {
    "1": ("200", None),
    "2": ("200", ""),
    "3": ("404", "error 200"),
    "4": ("404", None),
}

expected_outputs = {
    "1": "success",
    "2": "success",
    "3": "error 200",
    "4": "unexpected error",
}

assert complex_if_else(*test_cases["1"]) == expected_outputs["1"]
assert complex_if_else(*test_cases["2"]) == expected_outputs["2"]
assert complex_if_else(*test_cases["3"]) == expected_outputs["3"]
assert complex_if_else(*test_cases["4"]) == expected_outputs["4"]


# ## Solution 1: Guard and early return


def guard(response_status, response_error):
    if response_status != "200":
        if response_error is not None:
            return f"{response_error}"
        else:
            return "unexpected error"
    status = "success"
    return status


assert guard(*test_cases["1"]) == expected_outputs["1"]
assert guard(*test_cases["2"]) == expected_outputs["2"]
assert guard(*test_cases["3"]) == expected_outputs["3"]
assert guard(*test_cases["4"]) == expected_outputs["4"]
