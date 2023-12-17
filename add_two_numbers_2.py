# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1 = []
        while l1 is not None:
            r1.append(l1.val)
            l1 = l1.next
        r2 = []
        while l2 is not None:
            r2.append(l2.val)
            l2 = l2.next
        r1 = r1[::-1]
        r2 = r2[::-1]
        pos1 = 0
        pos2 = 0
        res = []
        remainder = 0
        while (pos1 < len(r1)) or (pos2 < len(r2)):
            if pos1 == len(r1):
                val1 = 0
            else:
                val1 = int(r1[pos1])
                pos1 += 1
            if pos2 == len(r2):
                val2 = 0
            else:
                val2 = int(r2[pos2])
                pos2 += 1
            remainder, temp = divmod(val1 + val2 + remainder, 10)
            res.append(str(temp))
        if remainder != 0:
            res.append(str(remainder))
        r = None
        for j in range(len(res)):
            r = ListNode(res[j], r)
        return r
