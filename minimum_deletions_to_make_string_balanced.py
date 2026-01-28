# You are given a string s consisting only of characters 'a' and 'b'​​​​.
# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
# Return the minimum number of deletions needed to make s balanced.
class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = 0
        b = 0
        for c in s:
            if c == "b":
                b += 1
            else:
                ans = min(ans + 1, b)
        return ans
