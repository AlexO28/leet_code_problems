# You are given two integer arrays of the same length nums1 and nums2. In one operation, you are allowed to swap nums1[i] with nums2[i].
# Return the minimum number of needed operations to make nums1 and nums2 strictly increasing. The test cases are generated so that the given input always makes it possible.
# An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1].
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        no_swap = 0
        swap = 1
        for i in range(1, len(nums1)):
            no_swap_cost = no_swap
            swap_cost = swap
            if (nums1[i-1] >= nums1[i]) or (nums2[i-1] >= nums2[i]):
                no_swap = swap_cost
                swap = no_swap_cost + 1
            else:
                swap = swap_cost + 1
                if (nums1[i-1] < nums2[i]) and (nums2[i-1] < nums1[i]):
                    no_swap = min(no_swap, swap_cost)
                    swap = min(swap, no_swap_cost + 1)
        return min(no_swap, swap)
