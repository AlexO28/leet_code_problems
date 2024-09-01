# Let's define a function countUniqueChars(s) that returns the number of unique characters in s.
# For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
# Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. The test cases are generated such that the answer fits in a 32-bit integer.
# Notice that some substrings can be repeated so in this case you have to count the repeated ones too.
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        if len(s) == 1:
            return 1
        index_map = {}
        for i in range(len(s)):
            if s[i] in index_map:
                index_map[s[i]].append(i)
            else:
                index_map[s[i]] = [i]
        number_of_characters = 0
        for indices in index_map.values():
            indices = [-1] + indices + [len(s)]
            for i in range(1, len(indices)-1):
                number_of_characters += (indices[i] - indices[i-1])*(indices[i+1] - indices[i])
        return number_of_characters
