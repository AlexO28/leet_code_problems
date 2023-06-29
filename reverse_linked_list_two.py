# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        arr_rev = []
        if right < len(arr):
            arr_rev.extend(arr[(right):][::-1])
        arr_rev.extend(arr[(left-1):(right)])
        if left > 1:
            arr_rev.extend(arr[:(left-1)][::-1])
        res = None
        for elem in arr_rev:
            res = ListNode(elem, res)
        return res
