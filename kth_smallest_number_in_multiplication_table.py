# Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).
# Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left = 1
        right = m * n
        while left < right:
            mid = (left + right) // 2
            count = 0
            for i in range(1, m + 1):
                count += min(mid // i, n)
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left
