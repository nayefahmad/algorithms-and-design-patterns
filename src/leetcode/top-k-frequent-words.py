"""
# Top K Frequent Words

Reference: leetcode problem 692

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with
the same frequency by their lexicographical order.

"""
import heapq
from collections import Counter, defaultdict
from typing import List


def topKFrequent(words: List[str], k: int) -> List[str]:
    counts = defaultdict(int)
    for word in words:
        counts[word] += 1

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


def counter_solution(words: List[str], k: int) -> List[str]:
    # todo: test this

    # Step 1: Count frequencies in O(n)
    counts = Counter(words)

    # Step 2: Sort words first by frequency (-count), then by lexicographical order
    sorted_words = sorted(counts.keys(), key=lambda word: (-counts[word], word))

    # Step 3: Return the top k words
    return sorted_words[:k]


def test_01():
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    result = topKFrequent(words, k)
    assert result == ["i", "love"]


def test_02():
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    result = topKFrequent(words, k)
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
    result = topKFrequent(words, k)
    assert result == ["is", "the", "sunny", "day"]


if __name__ == "__main__":
    test_02()
