# You are given the head of a linked list.
# Remove every node which has a node with a greater value anywhere to the right side of it.
# Return the head of the modified linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        if len(arr) > 1:
            new_arr = [arr[-1]]
            max_val = arr[-1]
            for j in range(len(arr)-2, -1, -1):
                if arr[j] >= max_val:
                    max_val = max(max_val, arr[j])
                    new_arr.append(max_val)
            arr = new_arr
        res = None
        for elem in new_arr:
            res = ListNode(elem, res)
        return res
