# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.
class Solution:
    def beautySum(self, s: str) -> int:
        ALPHABET = set(s)
        if len(ALPHABET) == 1:
            return 0
        prefix_sums = {}
        for element in ALPHABET:
            prefix_sums[element] = [0]
        for j in range(len(s)):
            for element in ALPHABET:
                if element == s[j]:
                    prefix_sums[element].append(prefix_sums[element][-1] + 1)
                else:
                    prefix_sums[element].append(prefix_sums[element][-1])
        res = 0
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                deltas = []
                for element in ALPHABET:
                    delta = prefix_sums[element][j + 1] - prefix_sums[element][i]
                    if delta > 0:
                        deltas.append(delta)
                if len(deltas) > 1:
                    res += max(deltas) - min(deltas)
        return res
