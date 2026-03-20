# Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.
# An alphanumeric string is a string consisting of lowercase English letters and digits.
class Solution:
    def secondHighest(self, s: str) -> int:
        arr = []
        for elem in s:
            try:
                arr.append(int(elem))
            except:
                continue
        arr = list(set(arr))
        if len(arr) <= 1:
            return -1
        else:
            arr.sort()
            return arr[-2]
