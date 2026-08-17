# You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.
# Return all lonely numbers in nums. You may return the answer in any order.
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        stats = Counter(nums)
        res = []
        for num in stats:
            if (
                (stats[num] == 1)
                and ((num + 1) not in stats)
                and ((num - 1) not in stats)
            ):
                res.append(num)
        return res
