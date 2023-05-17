# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str_arr = []
        for i in range(len(num1)):
            remainder = 0
            temp_str = ""
            if i > 0:
                temp_str += ''.join([str(0)]*i)
            for j in range(len(num2)):
                val = int(num1[len(num1)-i-1]) * int(num2[len(num2)-j-1]) + remainder
                remainder, value = divmod(val, 10)
                temp_str += str(value)
            if remainder > 0:
                temp_str += str(remainder)
            str_arr.append(temp_str[::-1])
        str_start = str_arr[0]
        for j in range(1, len(str_arr)):
            str_cur = str_arr[j]
            digits = max(len(str_start), len(str_cur))
            remainder = 0
            next_str = ""
            for i in range(digits):
                if len(str_start) - i - 1 >= 0:
                    val1 = int(str_start[len(str_start) - i - 1])
                else:
                    val1 = 0
                if len(str_cur) - i - 1 >= 0:
                    val2 = int(str_cur[len(str_cur) - i - 1])
                else:
                    val2 = 0
                remainder, value = divmod(val1 + val2 + remainder, 10)
                next_str += str(value)
 
            if remainder > 0:
                next_str += str(remainder)
            str_start = next_str[::-1]
        terminate = False
        for i in range(len(str_start)):
            if str_start[i] != "0":
                terminate = True
                break
        if terminate:
            return str_start[i:]
        else:
            return "0"
        return str_start
