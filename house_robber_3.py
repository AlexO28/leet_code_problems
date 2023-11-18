# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.
# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.rob_house(root))

    def rob_house(self, tree):
        if (tree.left is None) and (tree.right is None):
            return tree.val, 0
        elif (tree.left is not None) and (tree.right is not None):
            left_loot = self.rob_house(tree.left)
            right_loot = self.rob_house(tree.right)
            temp_val = left_loot[1] + right_loot[1] + tree.val
            second_cand = max(left_loot) + max(right_loot)
            return [temp_val, second_cand]
        elif tree.left is None:
            right_loot = self.rob_house(tree.right)
            temp_val = right_loot[1] + tree.val
            second_cand = max(right_loot[0], right_loot[1])
            return [temp_val, second_cand]
        else:
            left_loot = self.rob_house(tree.left)
            temp_val = left_loot[1] + tree.val
            second_cand = max(left_loot[0], left_loot[1])
            return [temp_val, second_cand]
  
