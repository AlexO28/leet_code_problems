# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_dict = {}
        for elem in allowed:
            if elem not in allowed_dict:
                allowed_dict[elem] = 1
        res = 0
        for word in words:
            fine = True
            for elem in word:
                if elem not in allowed_dict:
                    fine = False
                    break
            if fine:
                res += 1
        return res
