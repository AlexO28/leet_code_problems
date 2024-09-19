# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s == goal:
            s_dict = {}
            for elem in s:
                if elem in s_dict:
                    return True
                else:
                    s_dict[elem] = 1
            return False
        elif len(s) == len(goal):
            indices = []
            for i in range(len(s)):
                if s[i] != goal[i]:
                    indices.append(i)
                    if len(indices) > 2:
                        return False
            if (len(indices) <= 1):
                return False
            return (s[indices[0]] == goal[indices[1]]) and (s[indices[1]] == goal[indices[0]])
        else:
            return False
 
