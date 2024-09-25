# Given a balanced parentheses string s, return the score of the string.
# The score of a balanced parentheses string is based on the following rule:
# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        current = TreeNode()
        root = current  
        for i in range(len(s)):
            if (s[i] == '('): 
                child = TreeNode()
                child.setParent(current)
                current.addChild(child)
                current = child
            else:
                current = current.getParent()
        return root.computeScore()


class TreeNode:
    def __init__(self):
        self.parent = None
        self.children = []
 
    def addChild(self, node):         
        self.children.append(node)

    def setParent(self, node):     
        self.parent = node

    def getParent(self):     
        return self.parent
  
    def computeScore(self):         
        if (len(self.children) == 0):
            return 1
        res = 0
        for child in self.children:         
            res += child.computeScore()
        if (self.parent == None):
            return res
        else:
            return 2 * res
