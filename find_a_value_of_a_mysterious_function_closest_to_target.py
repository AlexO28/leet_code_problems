# Winston was given the above mysterious function func. He has an integer array arr and an integer target and he wants to find the values l and r that make the value |func(arr, l, r) - target| minimum possible.
# Return the minimum possible value of |func(arr, l, r) - target|.
# Notice that func should be called with the values l and r where 0 <= l, r < arr.length.
from typing import List


class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        min_difference = abs(arr[0] - target)
        current_and_values = {arr[0]}
        for num in arr:
            current_and_values = {
                num & prev_value for prev_value in current_and_values
            } | {num}
            min_difference = min(
                min_difference,
                min(abs(and_value - target) for and_value in current_and_values),
            )
        return min_difference
