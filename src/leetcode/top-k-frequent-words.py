"""
# Top K Frequent Words

Reference: leetcode problem 692

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with
the same frequency by their lexicographical order.

Notes:
    - Apparently a priority queue is a good way to solve this. In python, you can use
        the heapq built-in module to implement it.

"""
import pdb
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = {}
        seen = set()
        for idx_01 in range(len(words)):
            target = words[idx_01]
            if target not in seen:
                seen.add(target)
            else:
                continue

            for idx_02 in range(len(words)):
                if words[idx_02] == target:
                    if counts.get(words[idx_02]) is None:
                        counts[words[idx_02]] = 1
                    else:
                        counts[words[idx_02]] += 1
        pdb.set_trace()
        return counts


def test_01():
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    s = Solution()
    result = s.topKFrequent(words, k)
    assert result == ["i", "love"]


def test_02():
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    s = Solution()
    result = s.topKFrequent(words, k)
    assert result == ["the", "is", "sunny", "day"]


if __name__ == "__main__":
    test_02()
