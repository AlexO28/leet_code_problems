# You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :
# let x be the sum of all elements currently in your array.
# choose index i, such that 0 <= i < n and set the value of arr at index i to x.
# You may repeat this procedure as many times as needed.
# Return true if it is possible to construct the target array from arr, otherwise, return false.
from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        else:
            total_sum = sum(target)
            max_heap = [-num for num in target]
            heapify(max_heap)
            while -max_heap[0] > 1:
                max_element = -heappop(max_heap)
                remaining_sum = total_sum - max_element
                if remaining_sum == 1:
                    return True
                updated_element = max_element % remaining_sum
                if updated_element == 0 or updated_element == max_element:
                    return False
                heappush(max_heap, -updated_element)
                total_sum = total_sum - max_element + updated_element
            return True
