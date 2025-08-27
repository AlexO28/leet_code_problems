# Given a string s consisting only of characters a, b and c.
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a_list = []
        b_list = []
        c_list = []
        for j in range(len(s)):
            if s[j] == "a":
                a_list.append(j)
            elif s[j] == "b":
                b_list.append(j)
            else:
                c_list.append(j)
        pos = 0
        pos_a = 0
        pos_b = 0
        pos_c = 0
        count = 0
        while pos < len(s):
            while pos_a < len(a_list):
                if a_list[pos_a] >= pos:
                    break
                else:
                    pos_a += 1
            if pos_a == len(a_list):
                break
            while pos_b < len(b_list):
                if b_list[pos_b] >= pos:
                    break
                else:
                    pos_b += 1
            if pos_b == len(b_list):
                break
            while pos_c < len(c_list):
                if c_list[pos_c] >= pos:
                    break
                else:
                    pos_c += 1
            if pos_c == len(c_list):
                break
            count += len(s) - max(a_list[pos_a], b_list[pos_b], c_list[pos_c]) 
            pos += 1
        return count
