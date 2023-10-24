# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.extractLargestValues(root)

    def extractLargestValues(self, tree):
        arr = [tree.val]
        if (tree.left is not None) and (tree.right is not None):
            arr_left = self.extractLargestValues(tree.left)
            arr_right = self.extractLargestValues(tree.right)
            for i in range(0, min(len(arr_left), len(arr_right))):
                arr.append(max(arr_left[i], arr_right[i]))
            if len(arr_right) > len(arr_left):
                for i in range(len(arr_left), len(arr_right)):
                    arr.append(arr_right[i])
            elif len(arr_right) < len(arr_left):
                for i in range(len(arr_right), len(arr_left)):
                    arr.append(arr_left[i])
        elif tree.left is not None:
            arr_left = self.extractLargestValues(tree.left)
            arr.extend(arr_left)
        elif tree.right is not None:
            arr_right = self.extractLargestValues(tree.right)
            arr.extend(arr_right)
        return arr
