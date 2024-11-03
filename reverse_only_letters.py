# Given a string s, reverse the string according to the following rules:
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        start = 0
        end = len(s)-1
        res = []
        alphabet = set(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        while (end >= 0):
            if s[end] not in alphabet:
                res.append(s[end])
            else:
                while (start < len(s)):
                    if s[start] in alphabet:
                        break
                    else:
                        start += 1
                res.append(s[start])
                start += 1
            end -= 1
        return "".join(res[::-1])
