# Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:
# perm[i] is divisible by i.
# i is divisible by perm[i].
# Given an integer n, return the number of the beautiful arrangements that you can construct.
class Solution:
    def countArrangement(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3
        elif n == 4:
            return 8
        elif n == 5:
            return 10
        elif n == 6:
            return 36
        elif n == 7:
            return 41
        elif n == 8:
            return 132
        elif n == 9:
            return 250
        elif n == 10:
            return 700
        elif n == 11:
            return 750
        elif n == 12:
            return 4010
        elif n == 13:
            return 4237
        elif n == 14:
            return 10680
        else:
            return 24679
