# The power of the string is the maximum length of a non-empty substring that contains only one unique character.
# Given a string s, return the power of s.
class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 0
        charact = ""
        cur_power = 0
        for elem in s:
            if elem == charact:
                cur_power += 1
            else:
                charact = elem
                max_power = max(max_power, cur_power)
                cur_power = 1
        return max(max_power, cur_power)
