# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == 1:
            return "0"
        num = [int(elem) for elem in list(num)]
        i = 0
        while (len(num) > 0) & (k > 0):
            i = max(i, 0)
            if len(num) == 1:
                return "0"
            if i == len(num) - 1:
                k -= 1
                del num[i]
                i -= 1
                continue
            if num[i+1] < num[i]:
                k -= 1
                del num[i]
                i -= 1
                if num[0] == 0:
                    i = 0
                    found = False
                    while i < len(num):
                        if num[i] != 0:
                            found = True
                            break
                        i += 1
                    if found :
                        num = num[i:]
                        i = 0
                    else:
                        return "0"
            else:
                i += 1
        return ''.join([str(elem) for elem in num])
