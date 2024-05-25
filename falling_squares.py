# There are several squares being dropped onto the X-axis of a 2D plane.
# You are given a 2D integer array positions where positions[i] = [lefti, sideLengthi] represents the ith square with a side length of sideLengthi that is dropped with its left edge aligned with X-coordinate lefti.
# Each square is dropped one at a time from a height above any landed squares. It then falls downward (negative Y direction) until it either lands on the top side of another square or on the X-axis. A square brushing the left/right side of another square does not count as landing on it. Once it lands, it freezes in place and cannot be moved.
# After each square is dropped, you must record the height of the current tallest stack of squares.
# Return an integer array ans where ans[i] represents the height described above after dropping the ith square.
class Node:
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end
        self.mid = (start + end) >> 1
        self.value = 0
        self.add = 0

class SegmentTree:
    def __init__(self):
        self.root = Node(1, int(1e9))

    def modify(self, start, end, value, node=None):
        if start > end:
            return None
        if node is None:
            node = self.root
        if node.start >= start and node.end <= end:
            node.value = value
            node.add = value
            return None
        self.pushdown(node)
        if start <= node.mid:
            self.modify(start, end, value, node.left)
        if end > node.mid:
            self.modify(start, end, value, node.right)
        self.pushup(node)

    def query(self, start, end, node=None):
        if start > end:
            return 0
        if node is None:
            node = self.root
        if node.start >= start and node.end <= end:
            return node.value
        self.pushdown(node)
        max_value = 0
        if start <= node.mid:
            max_value = max(max_value, self.query(start, end, node.left))
        if end > node.mid:
            max_value = max(max_value, self.query(start, end, node.right))
        return max_value

    def pushup(self, node):
        node.value = max(node.left.value, node.right.value)

    def pushdown(self, node):
        if node.left is None:
            node.left = Node(node.start, node.mid)
        if node.right is None:
            node.right = Node(node.mid + 1, node.end)
        if node.add:
            node.left.value = node.add
            node.right.value = node.add
            node.left.add = node.add
            node.right.add = node.add
            node.add = 0

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        if len(positions) == 1:
            return [positions[0][1]]
        max_height = 0
        result = []
        tree = SegmentTree()
        for position in positions:
            right = position[0] + position[1] - 1
            height = tree.query(position[0], right) + position[1]
            max_height = max(max_height, height)
            result.append(max_height)
            tree.modify(position[0], right, height)
        return result
