# Let the function f(s) be the frequency of the lexicographically smallest character in a non-empty string s. For example, if s = "dcce" then f(s) = 2 because the lexicographically smallest character is 'c', which has a frequency of 2.
# You are given an array of strings words and another array of query strings queries. For each query queries[i], count the number of words in words such that f(queries[i]) < f(W) for each W in words.
# Return an integer array answer, where each answer[i] is the answer to the ith query.
import bisect
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        freqs = [self.countFrequency(word) for word in words]
        freqs.sort()
        return [len(words)-bisect.bisect_right(freqs, self.countFrequency(query)) for query in queries]

    def countFrequency(self, word):
        word = list(word)
        word.sort()
        freq = 0
        for elem in word:
            if elem == word[0]:
                freq += 1
            else:
                break
        return freq
