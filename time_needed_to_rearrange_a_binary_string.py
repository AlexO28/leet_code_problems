# You are given a binary string s.
# In one second, all occurrences of "01" are simultaneously replaced with "10". This process repeats until no occurrences of "01" exist.
# Return the number of seconds needed to complete this process.
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        res = 0
        while True:
            s_new = s.replace("01", "10")
            if s_new == s:
                return res
            else:
                res += 1
                s = s_new
