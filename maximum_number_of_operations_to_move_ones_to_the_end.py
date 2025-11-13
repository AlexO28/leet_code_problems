# You are given a binary string s.
# You can perform the following operation on the string any number of times:
# Choose any index i from the string where i + 1 < s.length such that s[i] == '1' and s[i + 1] == '0'.
# Move the character s[i] to the right until it reaches the end of the string or another '1'. For example, for s = "010010", if we choose i = 1, the resulting string will be s = "000110".
# Return the maximum number of operations that you can perform.
class Solution:
    def maxOperations(self, s: str) -> int:
        cur_block = 0
        sum_block = 0
        res = 0
        for elem in s:
            if elem == "1":
                cur_block += 1
            elif cur_block > 0:
                sum_block += cur_block
                res += sum_block
                cur_block = 0
        return res
