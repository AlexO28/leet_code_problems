# (This problem is an interactive problem.)
# You may recall that an array arr is a mountain array if and only if:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.
# You cannot access the mountain array directly. You may only access the array using a MountainArray interface:
# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) > mountainArr.get(mid + 1):
                right = mid
            else:
                left = mid + 1
        peak = left
        res = self.binary_search(0, peak, 1, mountainArr, target)
        if res == -1:
            res = self.binary_search(peak + 1, n - 1, -1, mountainArr, target)
        return res


    def binary_search(self, left, right, direction_factor, mountainArr, target):
        while abs(right - left) > 1:
            mid = (left + right) // 2
            if direction_factor > 0:
                if mountainArr.get(mid) >= target:
                    right = mid
                else:
                    left = mid
            else:
                if mountainArr.get(mid) >= target:
                    left = mid
                else:
                    right = mid
        if mountainArr.get(left) == target:
            return left
        elif mountainArr.get(right) == target:
            return right
        else:
            return -1
