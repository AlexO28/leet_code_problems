# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        arr = []
        temp = head
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
        if len(arr) == 1:
            return head
        arr_odd = [arr[i] for i in range(len(arr)) if i % 2 == 0]
        arr_even = [arr[i] for i in range(len(arr)) if i % 2 == 1]
        arr_odd.extend(arr_even)
        head = None
        for j in range(len(arr_odd)):
            head = ListNode(arr_odd[len(arr_odd)-j-1], head)
        return head
