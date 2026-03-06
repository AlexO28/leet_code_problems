# Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s) == 1:
            return True
        number_of_segments = 0
        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i - 1] == "1":
                    number_of_segments += 1
                    if number_of_segments == 2:
                        return False
        if s[-1] == "1":
            number_of_segments += 1
        return number_of_segments < 2
