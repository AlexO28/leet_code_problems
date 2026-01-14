# Write an API that generates fancy sequences using the append, addAll, and multAll operations.
# Implement the Fancy class:
# Fancy() Initializes the object with an empty sequence.
# void append(val) Appends an integer val to the end of the sequence.
# void addAll(inc) Increments all existing values in the sequence by an integer inc.
# void multAll(m) Multiplies all existing values in the sequence by an integer m.
# int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is greater or equal than the length of the sequence, return -1.
class Fancy:
    def __init__(self):
        self.n = 0
        self.tree = SegmentTree()

    def append(self, val: int) -> None:
        self.n += 1
        self.tree.modifyAdd(self.n, self.n, val)

    def addAll(self, inc: int) -> None:
        self.tree.modifyAdd(1, self.n, inc)

    def multAll(self, m: int) -> None:
        self.tree.modifyMul(1, self.n, m)

    def getIndex(self, idx: int) -> int:
        return -1 if idx >= self.n else self.tree.query(idx + 1, idx + 1)


class SegmentTree:
    def __init__(self):
        self.root = Node(1, int(1e5 + 1))
        self.MOD = 1000000007

    def modifyAdd(self, l, r, inc, node=None):
        if l > r:
            return
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            node.v = (node.v + (node.r - node.l + 1) * inc) % self.MOD
            node.add += inc
            return
        self.pushdown(node)
        if l <= node.mid:
            self.modifyAdd(l, r, inc, node.left)
        if r > node.mid:
            self.modifyAdd(l, r, inc, node.right)
        self.pushup(node)

    def modifyMul(self, l, r, m, node=None):
        if l > r:
            return
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            node.v = (node.v * m) % self.MOD
            node.add = (node.add * m) % self.MOD
            node.mul = (node.mul * m) % self.MOD
            return
        self.pushdown(node)
        if l <= node.mid:
            self.modifyMul(l, r, m, node.left)
        if r > node.mid:
            self.modifyMul(l, r, m, node.right)
        self.pushup(node)

    def query(self, l, r, node=None):
        if l > r:
            return 0
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            return node.v
        self.pushdown(node)
        v = 0
        if l <= node.mid:
            v = (v + self.query(l, r, node.left)) % self.MOD
        if r > node.mid:
            v = (v + self.query(l, r, node.right)) % self.MOD
        return v

    def pushup(self, node):
        node.v = (node.left.v + node.right.v) % self.MOD

    def pushdown(self, node):
        if node.left is None:
            node.left = Node(node.l, node.mid)
        if node.right is None:
            node.right = Node(node.mid + 1, node.r)
        left, right = node.left, node.right
        if node.add != 0 or node.mul != 1:
            left.v = (left.v * node.mul + (left.r - left.l + 1) * node.add) % self.MOD
            right.v = (
                right.v * node.mul + (right.r - right.l + 1) * node.add
            ) % self.MOD
            left.add = (left.add * node.mul + node.add) % self.MOD
            right.add = (right.add * node.mul + node.add) % self.MOD
            left.mul = (left.mul * node.mul) % self.MOD
            right.mul = (right.mul * node.mul) % self.MOD
            node.add = 0
            node.mul = 1


class Node:
    def __init__(self, l, r):
        self.left = None
        self.right = None
        self.l = l
        self.r = r
        self.mid = (l + r) >> 1
        self.v = 0
        self.add = 0
        self.mul = 1

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
