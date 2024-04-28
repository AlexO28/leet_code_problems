# Given the root of a binary tree, return the maximum width of the given tree.
# The maximum width of a tree is the maximum width among all levels.
# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        q = deque([(root, 0)])
        while len(q) > 0:
            size = len(q)
            cur_min = q[0][1]
            left_most = None
            right_most = None
            for i in range(size):
                cur_id = q[0][1] - cur_min
                temp1, temp2 = q.popleft()
                if i == 0:
                    left_most = cur_id
                if i == size - 1:
                    right_most = cur_id
                if temp1.left is not None:
                    q.append((temp1.left, cur_id * 2 + 1))
                if temp1.right is not None:
                    q.append((temp1.right, cur_id * 2 + 2))
            ans = max(ans, right_most - left_most + 1)
        return ans
