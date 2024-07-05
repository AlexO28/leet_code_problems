# A critical point in a linked list is defined as either a local maxima or a local minima.
# A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
# A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
# Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = self.listToArr(head)[::-1]
        if len(arr) < 3:
            return [-1, -1]
        critical_points = []
        for j in range(1, len(arr)-1):
            if (arr[j] > arr[j-1]) and (arr[j] > arr[j+1]):
                critical_points.append(j)
            elif (arr[j] < arr[j-1]) and (arr[j] < arr[j+1]):
                critical_points.append(j)
        if len(critical_points) < 2:
            return [-1, -1]
        return min([critical_points[j] - critical_points[j-1] for j in range(1, len(critical_points))]), critical_points[-1]-critical_points[0]

    def listToArr(self, head):
        if head.next is None:
            return [head.val]
        else:
            arr = self.listToArr(head.next)
            arr.append(head.val)
            return arr
