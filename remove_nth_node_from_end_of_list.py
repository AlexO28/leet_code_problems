# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = 0
        head_copy = head
        the_list = []
        while head_copy is not None:
            the_list.append(head_copy.val)
            head_copy = head_copy.next
        if len(the_list) == 0:
            return head
        pos = len(the_list) - n
        del the_list[pos]
        if len(the_list) == 0:
            return None
        else:
            iter = None
            for j in range(len(the_list)):
                node = ListNode(the_list[len(the_list)-j-1], iter)
                iter = node
        return iter
