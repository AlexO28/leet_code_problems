# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        got_second = False
        first_element = head.val
        res_list = []
        while head is not None:
            if got_second:
                got_second = False
                res_list.append(head.val)
                res_list.append(first_element)
            else:
                got_second = True
                first_element = head.val
            head = head.next
        if got_second:
            res_list.append(first_element)
        results = None
        for j in range(len(res_list)):
            results = ListNode(res_list[len(res_list)-1-j], results)
        return results
