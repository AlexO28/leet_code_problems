# You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.
# For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
# Return the head of the modified linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.arr = []
        self.add_next = True
        self.parseList(head)
        res = None
        for elem in self.arr[::-1]:
            res = ListNode(elem, res)
        return res
    
    def parseList(self, head):
        if head.val == 0:
            self.add_next = True
        else:
            if self.add_next:
                self.arr.append(head.val)
                self.add_next = False
            else:
                self.arr[-1] += head.val
        if head.next is not None:
            self.parseList(head.next)
