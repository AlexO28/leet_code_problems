# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head
        list_left = []
        list_right = []
        while head is not None:
            if head.val < x:
                list_left.append(head.val)
            else:
                list_right.append(head.val)
            head = head.next
        list_left.extend(list_right)
        list_left = list_left[::-1]
        res = None
        for element in list_left:
            res = ListNode(element, res)
        return res
