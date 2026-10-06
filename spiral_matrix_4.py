# You are given two integers m and n, which represent the dimensions of a matrix.
# You are also given the head of a linked list of integers.
# Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
# Return the generated matrix.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode | None) -> list[list[int]]:
        res = [[-1] * n for _ in range(m)]
        i = 0
        j = 0
        k = 0
        dirs = (0, 1, 0, -1, 0)
        while True:
            res[i][j] = head.val
            head = head.next
            if head is None:
                break
            while True:
                x = i + dirs[k]
                y = j + dirs[k + 1]
                if 0 <= x < m and 0 <= y < n and res[x][y] == -1:
                    i = x
                    j = y
                    break
                k += 1
                if k == 4:
                    k = 0
        return res
