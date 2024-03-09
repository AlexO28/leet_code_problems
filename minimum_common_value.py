# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        i1 = 0
        i2 = 0
        while (i1 < len(nums1)) and (i2 < len(nums2)):
            if nums1[i1] == nums2[i2]:
                return nums1[i1]
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        return -1
 
