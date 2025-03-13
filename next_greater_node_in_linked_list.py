# You are given the head of a linked list with n nodes.
# For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.
# Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, List


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        if len(arr) == 0:
            return [0]
        stack = []
        answer = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            if stack:
                answer[i] = stack[-1]          
            stack.append(arr[i])
        return answer
