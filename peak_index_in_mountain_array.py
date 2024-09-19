# You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.
# Return the index of the peak element.
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr)-1):
            if arr[i+1] < arr[i]:
                return i
        return len(arr)-1
