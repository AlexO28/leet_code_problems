# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        storage = []
        temp = head
        while temp is not None:
            storage.append(temp.val)
            temp = temp.next
        storage_new = []
        counter = 0
        for i in range(len(storage)):
            if i % 2 == 0:
                storage_new.append(storage[counter])
            else:
                storage_new.append(storage[len(storage)-1-counter])
                counter += 1
        temp = head
        counter = 0
        while temp is not None:
            temp.val = storage_new[counter]
            counter += 1 
            temp = temp.next
