# There are n uniquely-sized sticks whose lengths are integers from 1 to n. You want to arrange the sticks such that exactly k sticks are visible from the left. A stick is visible from the left if there are no longer sticks to the left of it.
# For example, if the sticks are arranged [1,3,2,5,4], then the sticks with lengths 1, 3, and 5 are visible from the left.
# Given n and k, return the number of such arrangements. Since the answer may be large, return it modulo 109 + 7.
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        f = [1] + [0] * k
        for i in range(1, n + 1):
            for j in range(k, 0, -1):
                f[j] = (f[j] * (i - 1) + f[j - 1]) % 1000000007
            f[0] = 0
        return f[k]
