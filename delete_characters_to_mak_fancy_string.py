# A fancy string is a string where no three consecutive characters are equal.
# Given a string s, delete the minimum possible number of characters from s to make it fancy.
# Return the final string after the deletion. It can be shown that the answer will always be unique.
class Solution:
    def makeFancyString(self, s: str) -> str:
        prev_elem = ""
        cur_freq = 0
        new_line = []
        for elem in s:
            if elem == prev_elem:
                cur_freq += 1
                if cur_freq <= 2:
                    new_line.append(elem)
            else:
                prev_elem = elem
                cur_freq = 1
                new_line.append(elem)
        return "".join(new_line)
