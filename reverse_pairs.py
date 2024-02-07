# Given an integer array nums, return the number of reverse pairs in the array.
# A reverse pair is a pair (i, j) where:
# 0 <= i < j < nums.length and nums[i] > 2 * nums[j].
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        return self.mergeSort(nums, 0, len(nums)-1)

    def mergeSort(self, nums, low, high):
        cnt = 0
        if low >= high:
            return cnt
        mid = (low + high) // 2
        cnt += self.mergeSort(nums, low, mid)
        cnt += self.mergeSort(nums, mid+1, high)
        cnt += self.countReversePairs(nums, low, mid, high)
        nums = self.merge(nums, low, mid, high);
        return cnt

    def countReversePairs(self, nums, low, mid, high):
        right = mid + 1
        cnt = 0
        for i in range(low, mid+1):
            while (right <= high) and (nums[i] > 2*nums[right]):
                right += 1
            cnt += (right - (mid + 1))
        return cnt

    def merge(self, nums, low, mid, high):
        temp = [0]*(high-low+1)
        i = low
        j = mid + 1
        k = 0
        while (i <= mid) and (j <= high):
            if nums[i] < nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
            k += 1
        while i <= mid:
            temp[k] = nums[i]
            k += 1
            i += 1
        while j <= high:
            temp[k] = nums[j]
            k += 1
            j += 1
        ind = 0
        for i in range(low, high+1):
            nums[i] = temp[ind]
            ind += 1
        return nums
