# You are given two integer arrays nums1 and nums2 of lengths m and n respectively. nums1 and nums2 represent the digits of two numbers. You are also given an integer k.
# Create the maximum number of length k <= m + n from digits of the two numbers. The relative order of the digits from the same array must be preserved.
# Return an array of the k digits representing the answer.

class Solution:

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        return self.create_max_number(0, 0, k,
            {}, nums1, nums2)

    def create_max_number(self, i1, i2, n, dp, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1 + l2

        if (i1, i2) in dp:
            return dp[(i1, i2)]
        if n == 0:
            return []
        max_searchable_length = l - i1 - i2 + 1 - n
        if max_searchable_length == 1:
            return self.merge(nums1[i1:], nums2[i2:])

        candidate_index_1 = self.info_on_max(nums1, i1,
            i1 + max_searchable_length)
        candidate_index_2 = self.info_on_max(nums2, i2,
            i2 + max_searchable_length)
        candidate_1 = nums1[candidate_index_1] if candidate_index_1 >= 0 else -1
        candidate_2 = nums2[candidate_index_2] if candidate_index_2 >= 0 else -1

        if candidate_1 > candidate_2:
            ret = [candidate_1] +\
                self.create_max_number(candidate_index_1 + 1, i2, n - 1,
                    dp, nums1, nums2)
        elif candidate_2 > candidate_1:
            ret = [candidate_2] +\
                self.create_max_number(i1, candidate_index_2 + 1, n - 1,
                    dp, nums1, nums2)
        else:
            try1 = self.create_max_number(candidate_index_1 + 1, i2, n - 1,
                    dp, nums1, nums2)
            try2 = self.create_max_number(i1, candidate_index_2 + 1, n - 1,
                    dp, nums1, nums2)
            if try1 > try2:
                ret = [candidate_1] + try1
            else:
                ret = [candidate_2] + try2
        dp[(i1, i2)] = ret
        return ret


    def merge(self, nums1, nums2):
        i1 = 0
        i2 = 0
        res = []
        while len(res) < len(nums1) + len(nums2):
            j1 = i1
            j2 = i2
            while (j1 < len(nums1)) and\
                  (j2 < len(nums2)) and\
                  (nums1[j1] == nums2[j2]):
                j1 += 1
                j2 += 1
            if (j2 == len(nums2)) or\
                ((j1 < len(nums1)) and (nums1[j1] > nums2[j2])):
                res.append(nums1[i1])
                i1 += 1
            else:
                res.append(nums2[i2])
                i2 += 1
        return res

    def info_on_max(self, nums, start, end):
        if start >= end or start >= len(nums):
            return -1
        max_index = start
        for i in range(start + 1, min(len(nums), end)):
            if nums[i] > nums[max_index]:
                max_index = i
        return max_index
