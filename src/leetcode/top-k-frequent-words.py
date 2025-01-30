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
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = {}
        seen = set()  # lookups for sets are O(1), vs for lists they are O(n)
        for x1 in range(len(words)):
            target = words[x1]
            if target not in seen:
                seen.add(target)
            else:
                continue

            for x2 in range(len(words)):
                if words[x2] == target:
                    if counts.get(words[x2]) is None:
                        counts[words[x2]] = 1
                    else:
                        counts[words[x2]] += 1

        counts_sorted = []
        for item in counts.items():
            word = item[0]
            count = item[1]
            heapq.heappush(counts_sorted, tuple([count * -1, word]))

        result = []
        for x3 in range(k):
            count_negated, word = heapq.heappop(counts_sorted)
            result.append(word)

        return result


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


def test_03():
    words = [
        "the",
        "day",
        "is",
        "is",
        "sunny",
        "the",
        "the",
        "the",
        "sunny",
        "is",
        "is",
    ]
    k = 4
    s = Solution()
    result = s.topKFrequent(words, k)
    assert result == ["is", "the", "sunny", "day"]


if __name__ == "__main__":
    test_02()
