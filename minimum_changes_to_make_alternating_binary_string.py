# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.
# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.
# Return the minimum number of operations needed to make s alternating.
class Solution:
    def minOperations(self, s: str) -> int:
        way_1 = 0
        way_2 = 0
        for j in range(len(s)):
            if j % 2 == 0:
                if s[j] == "0":
                    way_1 += 1
                else:
                    way_2 += 1
            else:
                if s[j] == "1":
                    way_1 += 1
                else:
                    way_2 += 1
        return min(way_1, way_2)
