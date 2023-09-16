# You are given an integer array nums and two integers indexDiff and valueDiff.
# Find a pair of indices (i, j) such that:
# i != j,
# abs(i - j) <= indexDiff.
# abs(nums[i] - nums[j]) <= valueDiff, and
# Return true if such pair exists or false otherwise.

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        width = valueDiff + 1
        for n, i in enumerate(nums):
            bucket = i // width
            if bucket in buckets:
                return True
            else:
                buckets[bucket] = i
                if bucket - 1 in buckets and i - buckets[bucket-1] <= valueDiff:
                    return True
                if bucket + 1 in buckets and buckets[bucket+1] - i <= valueDiff:
                    return True
                if n >= indexDiff:
                    del buckets[nums[n-indexDiff] // width]
        return False
