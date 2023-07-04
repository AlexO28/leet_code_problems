# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
