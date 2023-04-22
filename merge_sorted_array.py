# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        the_list = []
        while (list1 is not None) or (list2 is not None):
            if (list1 is not None) and (list2 is not None):
                if (list1.val <= list2.val):
                    the_list.append(list1.val)
                    list1 = list1.next
                else:
                    the_list.append(list2.val)
                    list2 = list2.next
            elif (list1 is not None):
                the_list.append(list1.val)
                list1 = list1.next
            elif (list2 is not None):
                the_list.append(list2.val)
                list2 = list2.next
        iter = None
        if len(the_list) == 0:
            return iter
        for j in range(len(the_list)):
            iter = ListNode(the_list[len(the_list)-j-1], iter)
        return iter
