# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
# Define a pair (u, v) which consists of one element from the first array and one element from the second array.
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        priority_queue = []
        for i in range(min(len(nums1), k)):
            priority_queue.append([nums1[i] + nums2[0], i, 0])  
        heapq.heapify(priority_queue)
        pairs = []
        while priority_queue and k > 0:
            sum_pair, index1, index2 = heapq.heappop(priority_queue)
            pairs.append([nums1[index1], nums2[index2]])          
            k -= 1
            if index2 + 1 < len(nums2):
                heapq.heappush(priority_queue,
                               [nums1[index1] + nums2[index2 + 1], index1, index2 + 1])
        return pairs
