# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.
# Return the head of the linked list after doubling it.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        new_arr = []
        remainder = 0
        for elem in arr[::-1]:
            remainder, val = divmod(2*elem + remainder, 10)
            new_arr.append(val)
        if remainder > 0:
            new_arr.append(remainder)
        res = None
        for elem in new_arr:
            res = ListNode(elem, res)
        return res
