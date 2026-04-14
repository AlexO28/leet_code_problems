# You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.
# You must perform an operation shift(c, x), where c is a character and x is a digit, that returns the xth character after c.
# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with the result of the shift(s[i-1], s[i]) operation.
# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.
# Note that shift(c, x) is not a preloaded function, but an operation to be implemented as part of the solution.
class Solution:
    def replaceDigits(self, s: str) -> str:
        ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
        INVERSE_ALPHABET = {ALPHABET[j]: j for j in range(len(ALPHABET))}
        res = []
        j = 0
        while j < len(s):
            res.append(s[j])
            if j < len(s) - 1:
                res.append(ALPHABET[(INVERSE_ALPHABET[s[j]] + int(s[j + 1]))])
            j += 2
        return "".join(res)
