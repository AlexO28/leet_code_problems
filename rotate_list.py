# Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_list(head):
    temp = head
    res = []
    while temp is not None:
        res.append(temp.val)
        temp = temp.next
    return res


def get_list_node(standard_list):
    pointer = None
    for element in standard_list[::-1]:
        pointer = ListNode(val = element, next = pointer)
    return pointer


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        standard_list = get_list(head)
        n = len(standard_list)
        k = k % n
        if k == 0:
            return head
        if n == 1:
            return head
        standard_list = standard_list[(n-k):n] + standard_list[:(n-k)]
        return get_list_node(standard_list)
