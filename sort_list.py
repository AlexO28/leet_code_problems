# Given the head of a linked list, return the list after sorting it in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        arr.sort(reverse = True)
        res = None
        for elem in arr:
            res = ListNode(elem, res)
        return res
