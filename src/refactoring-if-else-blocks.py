# # Refactoring complex if-else blocks

# References:
# - [Sunny Sun on Medium](https://betterprogramming.pub/4-simple-and-effective-ways-to-avoid-too-many-ifs-with-typescript-89937c0f9a99)  # noqa
# - [Jan on Medium](https://janalmazora.medium.com/how-to-prevent-using-if-else-statements-in-your-code-7e05e43afde)  # noqa


def complex_if_else(response_status, response_error):
    status = ""
    if response_status == "200":
        status = "success"
    else:
        if response_error:
            status = f"{response_error}"
        else:
            status = "unexpected error"
    return status


assert complex_if_else(response_status="200", response_error=None) == "success"
assert complex_if_else(response_status="404", response_error="error 200") == "error 200"
assert complex_if_else(response_status="404", response_error=None) == "unexpected error"
