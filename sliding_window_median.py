# Return the median array for each window in the original array. 
import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])
        res = []
        for j in range(k, len(nums)+1):
            if j == len(nums):
                b = 0
            else:
                b = nums[j]
            a = nums[j-k]
            res.append((window[k // 2] + window[~(k // 2)]) / 2.0)
            window.remove(a)
            bisect.insort(window, b)
        return res
