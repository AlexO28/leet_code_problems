# Given an empty set of intervals, implement a data structure that can:
# Add an interval to the set of intervals.
# Count the number of integers that are present in at least one interval.
# Implement the CountIntervals class:
# CountIntervals() Initializes the object with an empty set of intervals.
# void add(int left, int right) Adds the interval [left, right] to the set of intervals.
# int count() Returns the number of integers that are present in at least one interval.
# Note that an interval [left, right] denotes all the integers x where left <= x <= right.
class CountIntervals:
    def __init__(self):
        self.tree = SegmentTree()
        self.max = 1000000000

    def add(self, left, right):
        self.tree.modify(left, right, 1)

    def count(self):
        return self.tree.query(1, self.max)


class SegmentTree:
    def __init__(self):
        self.max = 1000000001
        self.root = Node(1, self.max)

    def modify(self, l, r, v, node=None):
        if node is None:
            node = self.root
        if l > r:
            return
        if node.l >= l and node.r <= r:
            node.v = node.r - node.l + 1
            node.add = v
            return
        self.pushdown(node)
        if l <= node.mid:
            self.modify(l, r, v, node.left)
        if r > node.mid:
            self.modify(l, r, v, node.right)
        self.pushup(node)

    def query(self, l, r, node=None):
        if node is None:
            node = self.root
        if l > r:
            return 0
        if node.l >= l and node.r <= r:
            return node.v
        self.pushdown(node)
        v = 0
        if l <= node.mid:
            v += self.query(l, r, node.left)
        if r > node.mid:
            v += self.query(l, r, node.right)
        return v

    def pushup(self, node):
        node.v = node.left.v + node.right.v

    def pushdown(self, node):
        if node.left is None:
            node.left = Node(node.l, node.mid)
        if node.right is None:
            node.right = Node(node.mid + 1, node.r)
        if node.add != 0:
            left, right = node.left, node.right
            left.add = node.add
            right.add = node.add
            left.v = left.r - left.l + 1
            right.v = right.r - right.l + 1
            node.add = 0


class Node:
    __slots__ = ("left", "right", "l", "r", "mid", "v", "add")

    def __init__(self, l, r):
        self.left = None
        self.right = None
        self.l = l
        self.r = r
        self.mid = (l + r) // 2
        self.v = 0
        self.add = 0

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
