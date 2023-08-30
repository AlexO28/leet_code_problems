# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        arr = []
        while head is not None:
            if head.val != val:
                arr.append(head.val)
            head = head.next
        if len(arr) == 0:
            return None
        head = None
        for elem in arr[::-1]:
            head = ListNode(elem, head)
        return head
