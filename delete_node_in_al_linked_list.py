# There is a singly-linked list head and we want to delete a node node in it.
# You are given the node to be deleted node. You will not be given access to the first node of head.
# All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.
# Delete the given node. Note that by deleting the node, we do not mean removing it from memory.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node
        arr = []
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
        if len(arr) == 1:
            return None
        temp = node
        for j in range(1, len(arr)):
            temp.val = arr[j]
            if j == len(arr) - 1:
                temp.next = None
            temp = temp.next
