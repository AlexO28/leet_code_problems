# You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.
# Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.
class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        remap_max = None
        for elem in list(num_str):
            if elem != "9":
                remap_max = elem
                break
        for elem in list(num_str):
            if elem != "0":
                remap_min = elem
                break
        if remap_max is None:
            max_val = num
        else:
            max_val = int(
                "".join([elem for elem in list(num_str.replace(remap_max, "9"))])
            )
        return max_val - int(
            "".join([elem for elem in list(num_str.replace(remap_min, "0"))])
        )
