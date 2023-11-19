# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
# Implement the Solution class:
# Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
# int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.

import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        while head is not None:
            self.arr.append(head.val)
            head = head.next
        self.len = len(self.arr)
        self.pos = 0

    def getRandom(self) -> int:
        return self.arr[random.randint(0, self.len-1)]
