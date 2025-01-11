# Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        else:
            freq_dict = {}
            for elem in s:
                if elem in freq_dict:
                    freq_dict[elem] += 1
                else:
                    freq_dict[elem] = 1
            num = 0
            for key in freq_dict:
                if freq_dict[key] % 2 == 1:
                    num += 1
            return num <= k
 
