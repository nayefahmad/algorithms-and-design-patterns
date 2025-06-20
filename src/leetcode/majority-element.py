"""
# Majority Element

Reference: leetcode problem 169

Given array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may
assume that the majority element always exists in the array.
"""
from collections import Counter, defaultdict
import math
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = set(nums)
        counts = {k: 0 for k in elements}

        # If allowed to user collections.Counter, we could do:
        # counts = Counter(nums)

        seen_elements = {}
        for element in elements:
            if element in seen_elements:
                continue
            for num in nums:
                if element == num:
                    counts[element] += 1

        threshold = math.floor(len(nums)/2)  # todo: not used

        counts_values = list(counts.values())
        max_val = max(counts_values)

        top_nums = {counts[k]: k for k in counts.keys()}
        majority_element = top_nums[max_val]
        return majority_element

    def majority_boyer_moore(self, nums: List[int]) -> int:
        """
        Reference: https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm  # noqa
        Roughly, the idea is that the count of a candidate hits zero when it has been
        "counterbalanaced" by a different element (or combination of elements). So we
        can then reset `count` to zero. And then we start the process again.
        """
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else:
                count -= 1

        return candidate



if __name__ == '__main__':
    input = [3, 2, 3]
    s = Solution()
    x = s.majorityElement(input)
    x2 = s.majority_boyer_moore(input)
    print('done')
