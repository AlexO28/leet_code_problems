# You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string.
# Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            res = s
            for j in range(len(s)-1):
                s = s[1:] + s[0]
                res = min(res, s)
            return res
        else:
            return "".join(sorted(s))
