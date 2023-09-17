# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findRoute(self, tree, p):
        if tree.val == p:
            return [0]
        else:
            if tree.left is not None:
                res_left = self.findRoute(tree.left, p)
                if 0 in res_left:
                    res_left.insert(0, -1)
                    return res_left
            if tree.right is not None:
                res_right = self.findRoute(tree.right, p)
                if 0 in res_right:
                    res_right.insert(0, 1)
                    return res_right
            return []

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        route_p = self.findRoute(root, p.val)
        route_q = self.findRoute(root, q.val)
        route = []
        for i in range(min(len(route_p), len(route_q))):
            if route_p[i] == route_q[i]:
                route.append(route_p[i])
            else:
                break
        if len(route) == 0:
            return root
        else:
            temp = root
            for elem in route:
                if elem < 0:
                    temp = temp.left
                elif elem > 0:
                    temp = temp.right
            return temp
