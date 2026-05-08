# You are given a string num, representing a large integer, and an integer k.
# We call some integer wonderful if it is a permutation of the digits in num and is greater in value than num. There can be many wonderful integers. However, we only care about the smallest-valued ones.
# Return the minimum number of adjacent digit swaps that needs to be applied to num to reach the kth smallest wonderful integer.
# The tests are generated in such a way that kth smallest wonderful integer exists.
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        s = list(num)
        for i in range(k):
            self.next_permutation(s)
        d = [[] for _ in range(10)]
        idx = [0] * 10
        for i, c in enumerate(num):
            j = ord(c) - ord("0")
            d[j].append(i)
        arr = [0] * len(s)
        for i, c in enumerate(s):
            j = ord(c) - ord("0")
            arr[i] = d[j][idx[j]]
            idx[j] += 1
        return sum(arr[j] > arr[i] for i in range(len(s)) for j in range(i))

    def next_permutation(self, nums):
        i = len(nums) - 2
        while (i >= 0) and (nums[i] >= nums[i + 1]):
            i -= 1
        j = len(nums) - 1
        while (j >= 0) and (nums[j] <= nums[i]):
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1 : len(nums)] = nums[i + 1 : len(nums)][::-1]
