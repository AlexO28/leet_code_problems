# You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
# A substring is a contiguous sequence of characters within a string.
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for j in range(len(num)-1, -1, -1):
            if int(num[j]) % 2 == 1:
                return num[:(j+1)]
        return ""
