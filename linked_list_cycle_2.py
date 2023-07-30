# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        temp = head
        found = False
        saved_vals = []
        while temp is not None:
            if temp.val is None:
                found = True
                temp.val = 0
                break
            saved_vals.append(temp.val)
            temp.val = None
            temp = temp.next
        if not found:
            return None
        counter = 0
        while head is not None:
            if head.val is not None:
                head.val = saved_vals[counter]
                return head
            counter += 1
            head = head.next
