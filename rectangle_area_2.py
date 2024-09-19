# You are given a 2D array of axis-aligned rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] denotes the ith rectangle where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner.
# Calculate the total area covered by all rectangles in the plane. Any area covered by two or more rectangles should only be counted once.
# Return the total area. Since the answer may be too large, return it modulo 109 + 7.
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        segments = []
        all_y = set()
        for x1, y1, x2, y2 in rectangles:
            segments.append((x1, y1, y2, 1))
            segments.append((x2, y1, y2, -1))
            all_y.update([y1, y2])
        segments.sort()
        all_y = sorted(all_y)      
        tree = SegmentTree(all_y)
        y_to_index = {y: index for index, y in enumerate(all_y)}    
        answer = 0
        for i, (x, y1, y2, value) in enumerate(segments):
            if i:
                answer += tree.length * (x - segments[i - 1][0])
            tree.modify(1, y_to_index[y1], y_to_index[y2] - 1, value)      
        return answer % int(1e9 + 7)

class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.tree = [Node() for i in range(len(nums) - 1 << 2)]
        self.build(1, 0, len(nums) - 2)

    def build(self, index, left, right):
        self.tree[index].left = left
        self.tree[index].right = right
        if left != right:
            mid = (left + right) >> 1
            self.build(index << 1, left, mid)
            self.build(index << 1 | 1, mid + 1, right)

    def modify(self, index, left, right, value):
        if self.tree[index].left >= left and self.tree[index].right <= right:
            self.tree[index].count += value
        else:
            mid = (self.tree[index].left + self.tree[index].right) >> 1
            if left <= mid:
                self.modify(index << 1, left, right, value)
            if right > mid:
                self.modify(index << 1 | 1, left, right, value)
        self.pushup(index)

    def pushup(self, index):
        if self.tree[index].count:
            self.tree[index].total_length = self.nums[self.tree[index].right + 1] - self.nums[self.tree[index].left]
        elif self.tree[index].left == self.tree[index].right:
            self.tree[index].total_length = 0
        else:
            self.tree[index].total_length = self.tree[index << 1].total_length + self.tree[index << 1 | 1].total_length

    @property
    def length(self):
        return self.tree[1].total_length

class Node:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.count = 0
        self.total_length = 0
