# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        freq_dict = {}
        for num1 in nums1:
            for num2 in nums2:
                summa = num1 + num2
                if summa in freq_dict:
                    freq_dict[summa] += 1
                else:
                    freq_dict[summa] = 1
        count = 0
        for num3 in nums3:
            for num4 in nums4:
               summa = num3 + num4
               if -summa in freq_dict:
                   count += freq_dict[-summa]
        return count
