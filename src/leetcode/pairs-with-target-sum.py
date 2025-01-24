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


def nested_for_solution(input: List, target: int) -> List:
    pairs = []
    for idx1 in range(len(input)):
        for idx2 in range(len(input)):
            if idx1 == idx2:
                continue

            num1 = input[idx1]
            num2 = input[idx2]
            if num1 + num2 == target:
                result = tuple(sorted([num1, num2]))
                if result not in pairs:
                    pairs.append(result)
                break
    return pairs


def two_pointer_solution():
    pass


def test_01():
    input = [1, 2, 3, 4, 5, 6]
    target = 6
    pairs = nested_for_solution(input, target)
    assert pairs == [(1, 5), (2, 4)]


def test_02():
    input = [3, 2, 4, 6, 5, 1]
    target = 6
    pairs = nested_for_solution(input, target)
    assert pairs == [(2, 4), (1, 5)]


if __name__ == '__main__':
    input = [1, 2, 3, 4, 5, 6]
    target = 6
    pairs = nested_for_solution(input, target)
    assert pairs == [(1, 5), (2, 4)]