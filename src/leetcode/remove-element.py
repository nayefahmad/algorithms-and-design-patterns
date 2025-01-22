"""
# Remove Element

Reference: leetcode problem 27

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in
`nums` in-place. The order of the elements may be changed. Then return the number of
elements in `nums` which are not equal to `val`.

Consider the number of elements in nums which are not equal to val be k,
to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements
    which are not equal to val. The remaining elements of nums are not important as
    well as the size of nums.
- Return k.

Custom Judge:

The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int val = ...; // Value to remove
    int[] expectedNums = [...]; // The expected answer with correct length.
                                // It is sorted with no values equaling val.

    int k = removeElement(nums, val); // Calls your implementation

    assert k == expectedNums.length;
    sort(nums, 0, k); // Sort the first k elements of nums
    for (int i = 0; i < actualLength; i++) {
        assert nums[i] == expectedNums[i];
    }

If all assertions pass, then your solution will be accepted.
"""
from typing import List, Tuple


class Solution:
    def removeElement(self, nums: List[int], val: int) -> Tuple[List, int]:
        """
        This is an example of a two-pointer approach. The "pointers" are variables
        that represent indices in the array. They often move in different ways - e.g.
        one moves faster than the other (as in this solution), or one moves from a
        different direction.

        The approach is particularly useful for achieving O(n) runtime performance
        where a nested for loop would otherwise be used.
        """
        number_removed = 0
        for idx1 in range(len(nums)):
            no_remove = True if nums[idx1] != val else False
            if no_remove:
                # note that k and idx1 will start differing once the if condition
                # evaluates to False.
                nums[number_removed] = nums[idx1]
                number_removed += 1
        nums[number_removed:] = []
        nums.sort()
        return nums, number_removed


def test_01():
    nums = [3, 2, 2, 3]
    val = 3
    s = Solution()
    nums, k = s.removeElement(nums, val)
    assert k == 2
    assert nums[:2] == [2, 2]


def test_02():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    s = Solution()
    nums, k = s.removeElement(nums, val)
    assert k == 5
    assert nums[:5] == [0, 0, 1, 3, 4]


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    s = Solution()
    nums, k = s.removeElement(nums, val)
    print("done!")
