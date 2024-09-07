# Given a binary tree root and a linked list with head as the first node. 
# Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.
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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        return self.checkDownward(root, arr, [])

    def checkDownward(self, tree, arr, arr_init):
        if tree is None:
            return False
        arr_new = arr_init.copy()
        arr_new.append(tree.val)
        if len(arr_new) >= len(arr):
            arr_new = arr_new[(len(arr_new)-len(arr)):]
            if arr_new == arr:
                return True
        return self.checkDownward(tree.left, arr, arr_new) or self.checkDownward(tree.right, arr, arr_new)
        
