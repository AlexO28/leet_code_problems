# You are given two strings of the same length s1 and s2 and a string baseStr.
# We say s1[i] and s2[i] are equivalent characters.
# For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
# Equivalent characters follow the usual rules of any equivalence relation:
# Reflexivity: 'a' == 'a'.
# Symmetry: 'a' == 'b' implies 'b' == 'a'.
# Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
# For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.
# Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.parent = list(range(26))
        ord_a = ord('a')
        for i in range(len(s1)):
            parent_s1 = self.find_parent(ord(s1[i]) - ord('a'))
            parent_s2 = self.find_parent(ord(s2[i]) - ord('a'))
            if parent_s1 < parent_s2:
                self.parent[parent_s2] = parent_s1
            else:
                self.parent[parent_s1] = parent_s2
        result = []
        for char in baseStr:
            result.append(chr(self.find_parent(ord(char) - ord_a) + ord_a))
        return "".join(result)

    def find_parent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]
