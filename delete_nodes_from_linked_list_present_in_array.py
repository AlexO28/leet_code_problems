# You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        self.nums_dict = {}
        for num in nums:
            if num not in self.nums_dict:
                self.nums_dict[num] = 1
        return self.find_relevant_node(head)
        
    def find_relevant_node(self, head):
        while head is not None:
            if head.val not in self.nums_dict:
                return ListNode(head.val, self.find_relevant_node(head.next))
            else:
                head = head.next
        return None
