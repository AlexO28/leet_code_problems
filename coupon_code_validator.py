# You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:
# code[i]: a string representing the coupon identifier.
# businessLine[i]: a string denoting the business category of the coupon.
# isActive[i]: a boolean indicating whether the coupon is currently active.
# A coupon is considered valid if all of the following conditions hold:
# code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
# businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
# isActive[i] is true.
# Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category.
from typing import List


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        data = []
        for j in range(len(code)):
            if isActive[j]:
                if businessLine[j] in [
                    "electronics",
                    "grocery",
                    "pharmacy",
                    "restaurant",
                ]:
                    if len(code[j]) > 0:
                        new_code = code[j].replace("_", "")
                        if (len(new_code) == 0) or (new_code.isalnum()):
                            data.append([businessLine[j], code[j]])
        data.sort()
        return [elem[1] for elem in data]
