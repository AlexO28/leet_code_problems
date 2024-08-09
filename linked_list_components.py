# You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.
# Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            num_dict[num] = 1
        number_of_components = 0
        gap = True
        while head is not None:
            if head.val in num_dict:
                if gap:
                    gap = False
                    number_of_components += 1
            else:
                gap = True
            head = head.next
        return number_of_components
