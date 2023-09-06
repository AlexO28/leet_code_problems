# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
# Return an array of the k parts.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import numpy as np


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if head is None:
            heads = []
            for j in range(k):
                heads.append(head)
            return heads
        if k == 1:
            return [head]
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        list_len = len(arr)
        num_elements = int(np.ceil(list_len/k))
        i = 0
        heads = []
        counter = 0
        len_effective = list_len
        while counter < k:
            cur_head = None
            if i < list_len:
                arr_temp = arr[i:min(i+num_elements, list_len)]
                if len(arr_temp) > 0:
                    arr_temp = arr_temp[::-1]
                    for j in range(len(arr_temp)):
                        cur_head = ListNode(arr_temp[j], cur_head)
                i += num_elements
                len_effective -= num_elements
                if k-counter-1 > 0:
                    num_elements = int(np.ceil((len_effective)/(k - counter - 1)))
                else:
                    num_elements = 0
            heads.append(cur_head)
            counter += 1
        return heads
