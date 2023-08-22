# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def extractTreeData(self, tree):
        res_dict = {}
        if tree.left is not None:
            left_dict = self.extractTreeData(tree.left)
            left_key_max = max(left_dict.keys()) + 1
        else:
            left_dict = {}
            left_key_max = 0   
        if tree.right is not None:
            right_dict = self.extractTreeData(tree.right)
            right_key_max = max(right_dict.keys()) + 1
        else:
            right_dict = {}
            right_key_max = 0
        max_key = max(left_key_max, right_key_max)
        res_dict[max_key] = tree.val
        for key in range(0, max_key):
            if left_key_max == right_key_max:
                res_dict[key] = right_dict[key]
            elif left_key_max > right_key_max:
                key_left = key
                key_right = key - (left_key_max - right_key_max)
                if key_right >= 0:
                    res_dict[key] = right_dict[key_right]
                else:
                    res_dict[key] = left_dict[key]
            else:
                res_dict[key] = right_dict[key]
        return res_dict

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res_dict = self.extractTreeData(root)
        max_key = max(res_dict.keys())
        res = []
        for j in range(0, max_key+1):
            res.append(res_dict[max_key-j])
        return res
