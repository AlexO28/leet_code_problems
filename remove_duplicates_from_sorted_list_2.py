# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        arr.append(239)
        elem_prev = arr[0]
        new_arr = []
        duplication = False
        for elem in arr[1:]:
            if elem != elem_prev:
                if not duplication:
                    new_arr.append(elem_prev)
                duplication = False
                elem_prev = elem
            else:
                duplication = True        
        iter = None
        for element in new_arr[::-1]:
            iter = ListNode(element, iter)
        return iter
