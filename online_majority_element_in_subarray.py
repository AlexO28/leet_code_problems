# Design a data structure that efficiently finds the majority element of a given subarray.
# The majority element of a subarray is an element that occurs threshold times or more in the subarray.
# Implementing the MajorityChecker class:
# MajorityChecker(int[] arr) Initializes the instance of the class with the given array arr.
# int query(int left, int right, int threshold) returns the element in the subarray arr[left...right] that occurs at least threshold times, or -1 if no such element exists
from typing import List
from collections import defaultdict
from bisect import bisect_left


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.tree = SegmentTree(arr)
        self.index_dict = defaultdict(list)
        for index, value in enumerate(arr):
            self.index_dict[value].append(index)
        

    def query(self, left: int, right: int, threshold: int) -> int:
        majority_value, freq = self.tree.query(1, left + 1, right + 1)
        left_index = bisect_left(self.index_dict[majority_value], left)
        right_index = bisect_left(self.index_dict[majority_value], right + 1)
        if right_index - left_index >= threshold:
            return majority_value
        return -1


class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.tree_nodes = [Node() for i in range(len(nums) << 2)]
        self.build(1, 1, len(nums))

    def build(self, node, left, right):
        self.tree_nodes[node].left_child = left
        self.tree_nodes[node].right_child = right
        if left == right:
            self.tree_nodes[node].value = self.nums[left - 1]
            self.tree_nodes[node].count = 1
        else:
            mid = (left + right) >> 1
            self.build(node << 1, left, mid)
            self.build(node << 1 | 1, mid + 1, right)
            self.push_up(node)

    def query(self, node, left, right):
        if self.tree_nodes[node].left_child >= left and self.tree_nodes[node].right_child <= right:
            return self.tree_nodes[node].value, self.tree_nodes[node].count
        mid = (self.tree_nodes[node].left_child + self.tree_nodes[node].right_child) >> 1
        if right <= mid:
            return self.query(node << 1, left, right)
        if left > mid:
            return self.query(node << 1 | 1, left, right)
        value_left, count_left = self.query(node << 1, left, right)
        value_right, count_right = self.query(node << 1 | 1, left, right)
        if value_left == value_right:
            return value_left, count_left + count_right
        if count_left >= count_right:
            return value_left, count_left - count_right
        else:
            return value_right, count_right - count_left

    def push_up(self, node):
        left = node << 1
        right = node << 1 | 1
        if self.tree_nodes[left].value == self.tree_nodes[right].value:
            self.tree_nodes[node].value = self.tree_nodes[left].value
            self.tree_nodes[node].count = self.tree_nodes[left].count + self.tree_nodes[right].count
        elif self.tree_nodes[left].count >= self.tree_nodes[right].count:
            self.tree_nodes[node].value = self.tree_nodes[left].value
            self.tree_nodes[node].count = self.tree_nodes[left].count - self.tree_nodes[right].count
        else:
            self.tree_nodes[node].value = self.tree_nodes[right].value
            self.tree_nodes[node].count = self.tree_nodes[right].count - self.tree_nodes[left].count

class Node:
    def __init__(self):
        self.left_child = 0
        self.right_child = 0
        self.value = 0
        self.count = 0

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
