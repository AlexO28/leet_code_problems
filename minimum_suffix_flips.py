# You are given a 0-indexed binary string target of length n. You have another binary string s of length n that is initially set to all zeros. You want to make s equal to target.
# In one operation, you can pick an index i where 0 <= i < n and flip all bits in the inclusive range [i, n - 1]. Flip means changing '0' to '1' and '1' to '0'.
# Return the minimum number of operations needed to make s equal to target.
class Solution:
    def minFlips(self, target: str) -> int:
        target = list(target)
        j = 0
        while j < len(target):
            if target[j] == "1":
                break
            else:
                j += 1
        if j == len(target):
            return 0
        else:
            search_one = True
            res = 0
            while j < len(target):
                if search_one:
                    if target[j] == "0":
                        res += 1
                        search_one = False
                    else:
                        j += 1
                else:
                    if target[j] == "1":
                        res += 1
                        search_one = True
                    else:
                        j += 1
            if search_one:
                if target[-1] == "1":
                    res += 1
            else:
                if target[-1] == "0":
                    res += 1
            return res
