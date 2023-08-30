# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        head = None
        for elem in arr:
            head = ListNode(elem, head)
        return head
