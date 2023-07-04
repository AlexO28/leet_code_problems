# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderTraversal(self, tree, level):
        res = {level: [tree.val]}
        if tree.left is not None:
            res_left = self.levelOrderTraversal(tree.left, level + 1)
            for left_level in res_left.keys():
                res[left_level] = res_left[left_level]
        if tree.right is not None:
            res_right = self.levelOrderTraversal(tree.right, level + 1)
            for right_level in res_right.keys():
                if right_level not in res.keys():
                    res[right_level] = res_right[right_level]
                else:
                    res[right_level].extend(res_right[right_level])
        return res

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res_dict = self.levelOrderTraversal(root, 0)
        keys = list(res_dict.keys())
        keys.sort()
        res = []
        alternate = False
        for key in keys:
            if alternate:
                res.append(res_dict[key][::-1])
                alternate = False
            else:
                res.append(res_dict[key])
                alternate = True
        return res
