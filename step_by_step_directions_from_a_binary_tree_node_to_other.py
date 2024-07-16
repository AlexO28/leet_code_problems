# You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
# Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
# 'L' means to go from a node to its left child node.
# 'R' means to go from a node to its right child node.
# 'U' means to go from a node to its parent node.
# Return the step-by-step directions of the shortest path from node s to node t.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        tmpPath = []
        startPath = []
        destPath = []
        self.parseTree(root, startValue, tmpPath, startPath)
        self.parseTree(root, destValue, tmpPath, destPath)
        startPath = startPath[0]
        destPath = destPath[0]
        ind = 0
        while (ind < len(startPath)) and (ind < len(destPath)):
            if startPath[ind] == destPath[ind]:
                ind += 1
            else:
                break
        if ind > 0:
            if ind == len(startPath):
                startPath = ""
            else: 
                startPath = startPath[ind:]
            if ind == len(destPath):
                destPath = ""
            else:
                destPath = destPath[ind:]
        if len(startPath) > 0:
            startPath = "U"*len(startPath)
        return startPath + destPath

    def parseTree(self, cur, targetValue, path, ans):
        if cur.val == targetValue:
            ans.append(''.join(path))
        else:
            if (cur.left is not None) and (cur.right is None):
                path.append("L")
                self.parseTree(cur.left, targetValue, path, ans)
                path.pop(-1)
            elif (cur.left is None) and (cur.right is not None):
                path.append("R")
                self.parseTree(cur.right, targetValue, path, ans)
                path.pop(-1)
            elif (cur.left is not None) and (cur.right is not None):
                path.append("L")
                self.parseTree(cur.left, targetValue, path, ans)
                path[-1] = 'R'
                self.parseTree(cur.right, targetValue, path, ans)
                path.pop(-1)
