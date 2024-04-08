# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages_data = self.calculateAverages(root)
        res = []
        for average in averages_data:
            res.append(average[0]/average[1])
        return res

    def calculateAverages(self, tree):
        res = [[tree.val, 1]]
        if (tree.left is None) and (tree.right is None):
            return res
        elif (tree.left is not None) and (tree.right is None):
            res.extend(self.calculateAverages(tree.left))
        elif (tree.left is None) and (tree.right is not None):
            res.extend(self.calculateAverages(tree.right))
        else:
            res_left = self.calculateAverages(tree.left)
            res_right = self.calculateAverages(tree.right)
            min_val = min(len(res_left), len(res_right))
            for j in range(min_val):
                res.append([res_left[j][0] + res_right[j][0], res_left[j][1] + res_right[j][1]])
            if len(res_left) > min_val:
                for j in range(min_val, len(res_left)):
                    res.append(res_left[j])
            elif len(res_right) > min_val:
                for j in range(min_val, len(res_right)):
                    res.append(res_right[j])
        return res
