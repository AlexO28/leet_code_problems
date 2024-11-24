# You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such that all of these parts represent the same binary value.
# If it is possible, return any [i, j] with i + 1 < j, such that:
# arr[0], arr[1], ..., arr[i] is the first part,
# arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
# arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
# All three parts have equal binary values.
# If it is not possible, return [-1, -1].
# Note that the entire part is used when considering what binary value it represents. For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        total_ones, remainder = divmod(sum(arr), 3)
        if remainder != 0:
            return [-1, -1]
        if total_ones == 0:
            return [0, len(arr)-1]
        part1_index = self.find_partition(arr, 1)
        part2_index = self.find_partition(arr, total_ones + 1)
        part3_index = self.find_partition(arr, 2 * total_ones + 1)
        while (part3_index < len(arr)) and (arr[part1_index] == arr[part2_index]) and (arr[part1_index] == arr[part3_index]):
            part1_index += 1
            part2_index += 1
            part3_index += 1
        if part3_index == len(arr):
            return [part1_index - 1, part2_index]
        else:
            return [-1, -1]
                

    def find_partition(self, arr, target_sum):
        running_sum = 0
        for j in range(len(arr)):
            running_sum += arr[j]
            if running_sum == target_sum:
                return j
        return -1
