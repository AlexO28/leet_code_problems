# Given the head of a linked list head, in which each node contains an integer value.
# Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
# Return the linked list after insertion.
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        new_arr = []
        for j in range(len(arr)-1):
            new_arr.append(arr[j])
            new_arr.append(gcd(arr[j], arr[j+1]))
        new_arr.append(arr[-1])
        res = None
        for j in range(len(new_arr)):
            res = ListNode(new_arr[len(new_arr)-j-1], res)
        return res
