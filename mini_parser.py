# Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return the deserialized NestedInteger.
# Each element is either an integer or a list whose elements may also be integers or other lists.
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        stack = []
        for j in range(len(s)):
            if s[j] == '[':
                stack.append(NestedInteger())
                start = j + 1
            elif s[j] == ',':
                if j > start:
                    num = int(s[start:j])
                    stack[-1].add(NestedInteger(num))
                start = j + 1
            elif s[j] == ']':
                popped = stack.pop()
                if j > start:
                    num = int(s[start:j])
                    popped.add(NestedInteger(num))
                if stack:
                    stack[-1].add(popped)
                else:
                    return popped
                start = j + 1
 
