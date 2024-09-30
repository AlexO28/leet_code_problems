# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
# You can return the answer in any order.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.distances = {}
        self.fill_distances(root)
        target = target.val
        latest_old = [target]
        visited = [target]
        if k == 0:
            return latest_old
        for j in range(k):
            latest = []
            if len(latest_old) == 0:
                return []
            for node in latest_old:
                if node in self.distances:
                    for neighbor in self.distances[node]:
                        if neighbor not in visited:
                            latest.append(neighbor)
                            visited.append(neighbor)
            latest_old = latest.copy()
        return latest

    def fill_distances(self, tree):
        if tree.left is not None:
            if tree.val in self.distances:
                self.distances[tree.val].append(tree.left.val)
            else:
                self.distances[tree.val] = [tree.left.val]
            if tree.left.val in self.distances:
                self.distances[tree.left.val].append(tree.val)
            else:
                self.distances[tree.left.val] = [tree.val]
            self.fill_distances(tree.left)
        if tree.right is not None:
            if tree.val in self.distances:
                self.distances[tree.val].append(tree.right.val)
            else:
                self.distances[tree.val] = [tree.right.val]
            if tree.right.val in self.distances:
                self.distances[tree.right.val].append(tree.val)
            else:
                self.distances[tree.right.val] = [tree.val]
            self.fill_distances(tree.right)
