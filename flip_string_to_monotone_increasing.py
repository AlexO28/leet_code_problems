# A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
# Return the minimum number of flips to make s monotone increasing.
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        if len(s) == 1:
            return 0
        ones_to_left = [0]*(len(s)+1)
        zeros_to_right = [1]*(len(s)+1)
        min_flips = len(s)
        for i in range(1, len(s)+1):
            if s[i-1] == "1":
                ones_to_left[i] = ones_to_left[i-1] + 1
            else:
                ones_to_left[i] = ones_to_left[i-1]
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                zeros_to_right[i] = zeros_to_right[i+1] + 1
            else:
                zeros_to_right[i] = zeros_to_right[i+1]
        for i in range(len(s)+1):
            min_flips = min(min_flips, ones_to_left[i] + zeros_to_right[i])
        return min_flips-1
