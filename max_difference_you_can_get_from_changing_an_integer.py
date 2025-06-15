# You are given an integer num. You will apply the following steps to num two separate times:
# Pick a digit x (0 <= x <= 9).
# Pick another digit y (0 <= y <= 9). Note y can be equal to x.
# Replace all the occurrences of x in the decimal representation of num by y.
# Let a and b be the two results from applying the operation to num independently.
# Return the max difference between a and b.
# Note that neither a nor b may have any leading zeros, and must not be 0.
class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        res = [num]
        for x in range(10):
            for y in range(10):
                if x != y:
                    new_num = int(
                        "".join(
                            [elem for elem in list(num_str.replace(str(x), str(y)))]
                        )
                    )
                    if len(str(new_num)) == len(num_str):
                        res.append(new_num)
        res = list(set(res))
        if 0 in res:
            res.remove(0)
        return max(res) - min(res)
