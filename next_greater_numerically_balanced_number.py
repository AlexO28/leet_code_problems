# An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.
# Given an integer n, return the smallest numerically balanced number strictly greater than n.
from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        num = n + 1
        while True:
            freq_dict = Counter(str(num))
            found = False
            for key in freq_dict:
                if freq_dict[key] != int(key):
                    found = True
            if not found:
                return num
            num += 1
