# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def turn_array_into_list_node(arr):
    l3 = ListNode(arr[-1], None)
    if len(arr)>1:
        for j in range(len(arr)-2, -1, -1):
            l3 = ListNode(arr[j], l3)
    return l3


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        remainder = 0
        iterate_through_l1 = True
        iterate_through_l2 = True
        while True:
            if iterate_through_l1 & iterate_through_l2:
                div_part, mod_part = divmod(l1.val + l2.val + remainder, 10)
                arr.append(mod_part)
                remainder = div_part
            elif iterate_through_l1:
                div_part, mod_part = divmod(l1.val + remainder, 10)
                arr.append(mod_part)
                remainder = div_part
            elif iterate_through_l2:
                div_part, mod_part = divmod(l2.val + remainder, 10)
                arr.append(mod_part)
                remainder = div_part
            else:
                if remainder>0:
                    arr.append(remainder)
                    remainder = 0
                else:
                    break
            if iterate_through_l1:
                if l1.next is not None:
                    l1 = l1.next
                else:
                    iterate_through_l1 = False
            if iterate_through_l2:
                if l2.next is not None:
                    l2 = l2.next
                else:
                    iterate_through_l2 = False
        return turn_array_into_list_node(arr)
