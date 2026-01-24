# You are given two linked lists: list1 and list2 of sizes n and m respectively.
# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
# The blue edges and nodes in the following figure indicate the result:
# Build the result list and return its head.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        arr1 = []
        elem = list1
        while elem is not None:
            arr1.append(elem.val)
            elem = elem.next
        arr2 = []
        elem = list2
        while elem is not None:
            arr2.append(elem.val)
            elem = elem.next
        new_arr = arr1[:a]
        new_arr.extend(arr2)
        new_arr.extend(arr1[(b + 1) :])
        res = None
        for elem in new_arr[::-1]:
            res = ListNode(elem, res)
        return res
