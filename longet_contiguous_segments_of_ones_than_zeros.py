# Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.
# For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
# Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        if len(s) == 1:
            return s[0] == "1"
        best_ones = 0
        best_zeros = 0
        cur_ones = 0
        cur_zeros = 0
        search_symb = s[0]
        if search_symb == "1":
            cur_ones += 1
        else:
            cur_zeros += 1
        for j in range(1, len(s)):
            if s[j] == search_symb:
                if search_symb == "1":
                    cur_ones += 1
                else:
                    cur_zeros += 1
            else:
                if search_symb == "0":
                    best_zeros = max(best_zeros, cur_zeros)
                    cur_ones = 1
                    search_symb = "1"
                    cur_zeros = 0
                else:
                    best_ones = max(best_ones, cur_ones)
                    cur_zeros = 1
                    search_symb = "0"
                    cur_ones = 0
        if search_symb == "1":
            best_ones = max(best_ones, cur_ones)
        else:
            best_zeros = max(best_zeros, cur_zeros)
        return best_ones > best_zeros
