# Given a string s, determine if it is valid.
# A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:
# Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
# Return true if s is a valid string, otherwise, return false.
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 3 != 0:
            return False
        else:
            stack = []
            for elem in s:
                stack.append(elem)
                if len(stack) >= 3:
                    if (stack[-1] == "c") and (stack[-2] == "b") and (stack[-3] == "a"):
                        stack[-3:] = ""
            return not stack
