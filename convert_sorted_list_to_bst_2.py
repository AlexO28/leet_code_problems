# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def arrayToBST(self, arr):
        if len(arr) == 1:
            return TreeNode(arr[0], None, None)
        if len(arr) == 2:
            left_tree = TreeNode(arr[0], None, None)
            return TreeNode(arr[1], left_tree, None)
        if len(arr) == 3:
            left_tree = TreeNode(arr[0], None, None)
            right_tree = TreeNode(arr[2], None, None)
            return TreeNode(arr[1], left_tree, right_tree)
        if len(arr) % 2 == 0:
            mid_pos = int(len(arr)/2) - 1
        else:
            mid_pos = int(len(arr)/2)
        left_tree = self.arrayToBST(arr[:mid_pos])
        right_tree = self.arrayToBST(arr[(mid_pos + 1):])
        return TreeNode(arr[mid_pos], left_tree, right_tree)

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        return self.arrayToBST(arr)
