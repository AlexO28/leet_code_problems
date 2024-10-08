# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        occurence_list = []
        for j in range(len(s)):
            if s[j] == c:
                occurence_list.append(j)
        res = []
        for j in range(len(s)):
            res.append(min([abs(i-j) for i in occurence_list]))
        return res
