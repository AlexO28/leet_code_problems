# You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.
# When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.
# Return true if it is possible to form a palindrome string, otherwise return false.
# Notice that x + y denotes the concatenation of strings x and y.
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.check1(a, b) or self.check1(b, a)

    def check1(self, a, b):
        i = 0
        j = len(b) - 1
        while i < j and a[i] == b[j]:
            i += 1
            j -= 1
        return i >= j or self.check2(a, i, j) or self.check2(b, i, j)

    def check2(self, a, i, j):
        return a[i : j + 1] == a[i : j + 1][::-1]
