# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#
# You may not alter the values in the list's nodes, only nodes themselves may be changed.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        res_list = []
        pack = []
        while head is not None:
            if len(pack) <= k-1:
                pack.append(head.val)
            else:
                res_list.extend(pack[::-1])
                pack = [head.val]                
            head = head.next
        if len(pack) == k:
            res_list.extend(pack[::-1])
        elif len(pack) > 0:
            res_list.extend(pack)
        results = None
        for j in range(len(res_list)):
            results = ListNode(res_list[len(res_list)-j-1], results)
        return results
 
