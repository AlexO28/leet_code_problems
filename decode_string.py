# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
class Solution:
    def decodeString(self, s: str) -> str:
        return self.decode(s, 0)[0]

    def decode(self, s, start_pos):
        res_str = ""
        pos = start_pos
        while pos < len(s):
            if s[pos] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                prev_pos = pos
                while s[pos] != "[":
                    pos += 1
                num = int(s[prev_pos:(pos)])
                res, endpos = self.decode(s, pos+1)
                pos = endpos + 1
                res_str += res*num
            elif s[pos] == "]":
                return res_str, pos
            else:
                res_str += s[pos]
                pos += 1
        return res_str, len(s)
