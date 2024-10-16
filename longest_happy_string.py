# A string s is called happy if it satisfies the following conditions:
# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".
# A substring is a contiguous sequence of characters within a string.
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = []
        max_val = max(a, b, c)
        while max_val > 0:
            added = False
            if a == max_val:
                s, added = self.add_letter(s, "a")
                if added:
                    a -= 1
            if (not added) and (b == max_val):
                s, added = self.add_letter(s, "b")
                if added:
                    b -= 1
            if (not added) and (c == max_val):
                s, added = self.add_letter(s, "c")
                if added:
                    c -= 1
            if not added:
                elems = [elem for elem in [a, b, c] if elem < max_val]
                if len(elems) == 0:
                    return "".join(s)
                max_val = max(elems)
                if max_val <= 0:
                    return "".join(s)
                if a == max_val:
                    s, added = self.add_letter(s, "a")
                    if added:
                        a -= 1
                if (not added) and (b == max_val):
                    s, added = self.add_letter(s, "b")
                    if added:
                        b -= 1
                if (not added) and (c == max_val):
                    s, added = self.add_letter(s, "c")
                    if added:
                        c -= 1
            if not added:
                min_val = min(a, b, c)
                if min_val == max_val:
                    return "".join(s)
                max_val = min_val
                if max_val <= 0:
                    return "".join(s)
                if a == max_val:
                    s, added = self.add_letter(s, "a")
                    if added:
                        a -= 1
                if (not added) and (b == max_val):
                    s, added = self.add_letter(s, "b")
                    if added:
                        b -= 1
                if (not added) and (c == max_val):
                    s, added = self.add_letter(s, "c")
                    if added:
                        c -= 1
            if not added:
                return "".join(s)
            max_val = max(a, b, c)
        return "".join(s)    

    def add_letter(self, s, letter):
        found = False
        if len(s) < 2:
            s.append(letter)
            found = True
        else:
            if (s[-1] != letter) or (s[-2] != letter):
                s.append(letter)
                found = True
        return s, found
