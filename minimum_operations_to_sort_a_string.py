# You are given a string s consisting of lowercase English letters.
# In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order.
# Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1.
class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 1:
            return 0
        s_list = list(s)
        if s_list == sorted(s_list.copy()):
            return 0
        elif len(s) == 2:
            return -1
        else:
            min_val = min(s_list)
            max_val = max(s_list)
            if (min_val == s_list[0]) or (max_val == s_list[-1]):
                return 1
            elif (min_val in s_list[1:(-1)]) or (max_val in s_list[1:(-1)]):
                return 2
            else:
                return 3
        
