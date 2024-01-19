# You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:
# If nums[i] is positive, move nums[i] steps forward, and
# If nums[i] is negative, move nums[i] steps backward.
# Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.
# A cycle in the array consists of a sequence of indices seq of length k where:
# Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
# Every nums[seq[j]] is either all positive or all negative.
# k > 1
# Return true if there is a cycle in nums, or false otherwise.
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        visited = set()
        for i in range(len(nums)):
            if i in visited:
                continue
            visited.add(i)
            path = {i}
            last_j = i
            j = self.next_index(i, nums[i], len(nums))
            while (nums[i] > 0) == (nums[j] > 0):
                if j in path:
                    if last_j == j:
                        visited.add(j)
                        break
                    return True
                if j in visited:
                    break
                visited.add(j)
                path.add(j)
                last_j = j
                j = self.next_index(j, nums[j], len(nums))
            continue
        return False

    def next_index(self, ind, shift, num_len):
        return (ind + shift) % num_len
