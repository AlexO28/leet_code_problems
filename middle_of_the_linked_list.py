# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        save = head
        while save is not None:
            arr.append(save.val)
            save = save.next
        count = 0
        save = head
        while count < int(len(arr)/2):
            save = save.next
            count += 1
        return save
