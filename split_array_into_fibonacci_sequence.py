# You are given a string of digits num, such as "123456579". We can split it into a Fibonacci-like sequence [123, 456, 579].
# Formally, a Fibonacci-like sequence is a list f of non-negative integers such that:
# 0 <= f[i] < 2**31, (that is, each integer fits in a 32-bit signed integer type),
# f.length >= 3, and
# f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.
# Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.
# Return any Fibonacci-like sequence split from num, or return [] if it cannot be done.
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        res = []
        max_num = 2 ** 31
        if len(num) < 3:
            return []
        for i in range(len(num)-2):
            try:
                x_old = int(num[:(i+1)])
            except:
                continue
            if x_old >= max_num:
                continue
            if str(x_old) == num[:(i+1)]:
                for j in range(i+1, len(num)-1):
                    try:
                        y_old = int(num[(i+1):(j+1)])
                    except:
                        continue
                    if y_old >=  max_num:
                        continue
                    if str(y_old) == num[(i+1):(j+1)]:
                        res = [x_old, y_old]
                        x = res[0]
                        y = res[1]
                        k = j+1
                        found = True
                        while k < len(num):
                            z = x + y
                            if z >= max_num:
                                found = False
                                break
                            z_str = str(z)
                            k_new = k + len(z_str)
                            if k_new > len(num):
                                found = False
                                break
                            if z_str == num[k:(k_new)]:
                                k = k_new
                                res.append(z)
                                x, y = y, z
                            else:
                                found = False
                                break
                        if found:
                            return res
        return []
