# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null
# Note that the linked lists must retain their original structure after the function returns.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempX = headA
        vals = []
        while tempX is not None:
            vals.append(tempX.val)
            tempX.val = None
            tempX = tempX.next
        tempY = headB
        while tempY is not None:
            if tempY.val is None:
                tempY.val = 0
                break
            tempY = tempY.next
        tempX = headA
        value_to_return = None
        for i in range(len(vals)):
            val = vals[i]
            if tempX.val == 0:
                value_to_return = tempX
            tempX.val = val
            tempX = tempX.next
        return value_to_return
