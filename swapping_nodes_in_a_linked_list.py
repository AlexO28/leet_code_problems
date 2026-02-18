# You are given the head of a linked list, and an integer k.
# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        arr[k - 1], arr[-k] = arr[-k], arr[k - 1]
        res = None
        for elem in arr[::-1]:
            res = ListNode(elem, res)
        return res
