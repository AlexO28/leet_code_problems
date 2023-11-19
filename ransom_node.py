# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = {}
        magazine_dict = {}
        for elem in ransomNote:
            if elem in ransom_dict.keys():
                ransom_dict[elem] += 1
            else:
                ransom_dict[elem] = 1
        for elem in magazine:
            if elem in magazine_dict.keys():
                magazine_dict[elem] += 1
            else:
                magazine_dict[elem] = 1
        for key in ransom_dict.keys():
            if key not in magazine_dict.keys():
                return False
            if ransom_dict[key] > magazine_dict[key]:
                return False
        return True
