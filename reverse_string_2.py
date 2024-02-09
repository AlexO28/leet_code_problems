# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        reverse = True
        res = []
        while i < len(s):
            if reverse:
                res.append(s[i:(i+k)][::-1])
                reverse = False
            else:
                res.append(s[i:(i+k)])
                reverse = True
            i += k
        return "".join(res)
