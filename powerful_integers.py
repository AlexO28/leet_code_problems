# Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.
# An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.
# You may return the answer in any order. In your answer, each value should occur at most once.
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound == 0:
            return []
        xvals = self.form_values(x, bound)
        yvals = self.form_values(y, bound)
        res = []
        for xval in xvals:
            for yval in yvals:
                zval = xval + yval
                if zval <= bound:
                    res.append(zval)
                else:
                    break
        return list(set(res))

    def form_values(self, z, bound):
        res = [1]
        if z > 1:
            num = z
            while num <= bound:
                res.append(num)
                num *= z
        return res
