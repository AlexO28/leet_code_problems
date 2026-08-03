# You are given the head of a linked list.
# The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words,
# The 1st node is assigned to the first group.
# The 2nd and the 3rd nodes are assigned to the second group.
# The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
# Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.
# Reverse the nodes in each group with an even length, and return the head of the modified linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        target_len = 1
        group = []
        res = []
        for i in range(len(arr)):
            group.append(arr[i])
            if len(group) == target_len:
                if len(group) % 2 == 0:
                    res.extend(group[::-1])
                else:
                    res.extend(group)
                group = []
                target_len += 1
        if len(group) > 0:
            if len(group) % 2 == 0:
                res.extend(group[::-1])
            else:
                res.extend(group)
        res_list = None
        for elem in res[::-1]:
            res_list = ListNode(elem, res_list)
        return res_list
