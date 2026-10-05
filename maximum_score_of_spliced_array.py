# You are given two 0-indexed integer arrays nums1 and nums2, both of length n.
# You can choose two integers left and right where 0 <= left <= right < n and swap the subarray nums1[left...right] with the subarray nums2[left...right].
# You may choose to apply the mentioned operation once or not do anything.
# The score of the arrays is the maximum of sum(nums1) and sum(nums2), where sum(arr) is the sum of all the elements in the array arr.
# Return the maximum possible score.
# A subarray is a contiguous sequence of elements within an array. arr[left...right] denotes the subarray that contains the elements of nums between indices left and right (inclusive).
class Solution:
    def maximumsSplicedArray(self, nums1: list[int], nums2: list[int]) -> int:
        return max(
            sum(nums2) + self.calculate(nums1, nums2),
            sum(nums1) + self.calculate(nums2, nums1),
        )

    def calculate(self, nums1, nums2):
        d = [a - b for a, b in zip(nums1, nums2)]
        t = d[0]
        max_val = d[0]
        for v in d[1:]:
            if t > 0:
                t += v
            else:
                t = v
            max_val = max(max_val, t)
        return max_val
