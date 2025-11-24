# You are given a string s.
# A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.
# Return the number of good splits you can make in s.
class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) == 1:
            return 0
        else:
            s = list(s)
            s_left = {s[0]: 1}
            s_right = {}
            for j in range(1, len(s)):
                if s[j] in s_right:
                    s_right[s[j]] += 1
                else:
                    s_right[s[j]] = 1
            res = 0
            if len(s_left) == len(s_right):
                res += 1
            if len(s) > 2:
                for j in range(1, len(s) - 1):
                    if s[j] in s_left:
                        s_left[s[j]] += 1
                    else:
                        s_left[s[j]] = 1
                    if s_right[s[j]] == 1:
                        del s_right[s[j]]
                    else:
                        s_right[s[j]] -= 1
                    if len(s_left) == len(s_right):
                        res += 1
            return res
