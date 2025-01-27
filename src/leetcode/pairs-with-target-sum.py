"""
# Find unique pairs that sum to target value

This is not an actual leetcode problem, just a similar example.

Given an integer array A, sorted in ascending order, find all pairs of integers that
sum to a target value.

We will solve this using two different approaches:
- Nested for loop. This has O(n^2) runtime
- Two-pointer approach. This has O(n) runtime

"""
from typing import List

import pytest


def nested_for_solution(input: List, target: int) -> List:
    pairs = []
    for idx1 in range(len(input)):
        for idx2 in range(idx1 + 1, len(input)):
            num1 = input[idx1]
            num2 = input[idx2]
            if num1 + num2 == target:
                result = tuple(sorted([num1, num2]))
                if result not in pairs:
                    pairs.append(result)
                break
    return pairs


def two_pointer_solution(input: List, target: int) -> List:
    pairs = []
    left, right = 0, len(input) - 1
    while left < right:
        if input[left] + input[right] == target:
            result = tuple(sorted((input[left], input[right])))
            if result not in pairs:
                pairs.append(result)
            left += 1
            right -= 1
        elif input[left] + input[right] < target:
            left += 1
        elif input[left] + input[right] > target:
            right -= 1
    return pairs


# def hash_table_solution(input: List, target: int) -> List:
#     pass


@pytest.mark.parametrize("func", [nested_for_solution, two_pointer_solution])
def tests(func):
    test_cases = [
        # Each tuple has a tuple with 2 inputs, list with output
        (([1, 2, 3, 4, 5, 6], 6), [(1, 5), (2, 4)]),
        (([1, 2, 3, 4, 5, 6], 3), [(1, 2)]),
        (([1, 2, 3, 4, 5, 6], 13), []),
        (([1, 1, 2, 3, 4, 4, 5, 6], 6), [(1, 5), (2, 4)]),
    ]
    for test_case in test_cases:
        pairs = func(test_case[0][0], test_case[0][1])
        assert pairs == test_case[1]


if __name__ == "__main__":
    input = [1, 2, 3, 4, 5, 6]
    target = 6
    pairs = nested_for_solution(input, target)
    assert pairs == [(1, 5), (2, 4)]
