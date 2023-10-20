# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.
# Implement the NestedIterator class:
# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = self.parseList([], nestedList)
        self.pos = 0

    def next(self) -> int:
        self.pos += 1
        return self.arr[self.pos-1]
    
    def hasNext(self) -> bool:
        return self.pos < len(self.arr)

    def parseList(self, arr, nestedList):
        for elem in nestedList:
            elem_int = elem.getInteger()
            if elem_int is not None:
                arr.append(elem_int)
            else:
                elem = elem.getList()
                if elem is None:
                    break
                else:
                    arr = self.parseList(arr, elem)
        return arr

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
