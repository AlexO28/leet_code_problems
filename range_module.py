# A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.
# A half-open interval [left, right) denotes all the real numbers x where left <= x < right.
# Implement the RangeModule class:
# RangeModule() Initializes the object of the data structure.
# void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
# boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
# void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.is_covered = False
        self.lazy = 0

class SegmentTree:
    def __init__(self):
        self.root = Node()

    def modify(self, start, end, value, left=1, right=int(1e9), node=None):
        if node is None:
            node = self.root
        if left >= start and right <= end:
            node.lazy = value
            node.is_covered = (value == 1)
        else:
            self.pushdown(node)
            mid = (left + right) >> 1
            if start <= mid:
                self.modify(start, end, value, left, mid, node.left or Node())
            if end > mid:
                self.modify(start, end, value, mid + 1, right, node.right or Node())
            self.pushup(node)

    def query(self, start, end, left=1, right=int(1e9), node=None):
        if node is None:
            node = self.root
        if left >= start and right <= end:
            return node.is_covered
        self.pushdown(node)
        mid = (left + right) >> 1
        covered = True
        if start <= mid:
            covered = covered and (node.left and self.query(start, end, left, mid, node.left))
        if end > mid:
            covered = covered and (node.right and self.query(start, end, mid + 1, right, node.right))
        return covered

    def pushup(self, node):
        node.is_covered = (node.left and node.left.is_covered and node.right and node.right.is_covered)

    def pushdown(self, node):
        if not (node.left or node.right):
            node.left = Node()
            node.right = Node()
        if node.lazy:
            for child in [node.left, node.right]:
                child.lazy = node.lazy
                child.is_covered = (node.lazy == 1)
            node.lazy = 0

class RangeModule:

    def __init__(self):
        self.tree = SegmentTree()
        
    def addRange(self, left: int, right: int) -> None:
        self.tree.modify(left, right - 1, 1)

    def queryRange(self, left: int, right: int) -> bool:
        return self.tree.query(left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        self.tree.modify(left, right - 1, -1)
