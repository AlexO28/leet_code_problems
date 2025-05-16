# Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
# After doing so, return the head of the final linked list.  You may return any such answer.
# (Note that in the examples below, all sequences are serializations of ListNode objects.)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)
        prefix_sums = {}
        current_sum = 0
        current_node = dummy_node
        while current_node:
            current_sum += current_node.val
            prefix_sums[current_sum] = current_node
            current_node = current_node.next
        current_sum = 0
        current_node = dummy_node
        while current_node:
            current_sum += current_node.val
            current_node.next = prefix_sums[current_sum].next
            current_node = current_node.next
        return dummy_node.next
