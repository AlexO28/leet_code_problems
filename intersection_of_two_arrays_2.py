# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inpos1 = 0
        inpos2 = 0
        nums1.sort()
        nums2.sort()
        arr = []
        while True:
            if (inpos1 >= len(nums1)) or (inpos2 >= len(nums2)):
                break
            if nums1[inpos1] < nums2[inpos2]:
                inpos1 += 1
            elif nums1[inpos1] > nums2[inpos2]:
                inpos2 += 1
            else:
                arr.append(nums1[inpos1])
                inpos1 += 1
                inpos2 += 1
        return arr
