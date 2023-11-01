# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
# If the tree has more than one mode, return them in any order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr = self.treeToArr(root)
        arr_dict = {}
        max_val = 0
        for elem in arr:
            if elem in arr_dict.keys():
                arr_dict[elem] += 1
            else:
                arr_dict[elem] = 1
            max_val = max(max_val, arr_dict[elem])
        res = []
        for elem in arr_dict.keys():
            if arr_dict[elem] == max_val:
                res.append(elem)
        return res

    def treeToArr(self, tree):
        arr = [tree.val]
        if tree.left is not None:
            res_left = self.treeToArr(tree.left)
            arr.extend(res_left)
        if tree.right is not None:
            res_right = self.treeToArr(tree.right)
            arr.extend(res_right)
        return arr
 
