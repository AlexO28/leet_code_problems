# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        results = []
        positions = [0]*(len(lists))
        num = len(lists)
        positions_to_delete = []
        for j in range(num):
            if lists[j] is None:
                positions_to_delete.append(j)
        if len(positions_to_delete)>0:
            for position in positions_to_delete[::-1]:
                del lists[position]
                del positions[position]
        while len(positions)>0:
            num = len(positions)
            index = 0
            min_val = lists[0].val
            for j in range(num):
                if lists[j].val < min_val:
                    index = j
                    min_val = lists[j].val
            results.append(min_val)
            positions[index] += 1
            lists[index] = lists[index].next
            if lists[index] is None:
                del positions[index]
                del lists[index]
        if len(results) == 0:
            return None
        resNode = ListNode(results[len(results)-1], None)
        if len(results) == 1:
            return resNode
        for j in range(0, len(results)-1):
            resNode = ListNode(results[len(results)-2-j], resNode)
        return resNode
