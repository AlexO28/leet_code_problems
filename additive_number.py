# An additive number is a string whose digits can form an additive sequence.
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
# Given a string containing only digits, return true if it is an additive number or false otherwise.
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        for pos1 in range(len(num)-2):
            for pos2 in range(pos1+1, len(num)-1):
                num1 = num[:(pos1+1)]
                if (len(num1) == 1) or (num1[0] != "0"):
                    num1 = int(num1)
                    num2 = num[(pos1+1):(pos2+1)]
                    if (len(num2) == 1) or (num2[0] != "0"):
                        num2 = int(num2)
                        prev1 = num1
                        prev2 = num2
                        ind = pos2 + 1
                        terminate = False
                        while True:
                            if ind >= len(num):
                                return True
                            num_next = prev1 + prev2
                            num_next_str = str(num_next)
                            if ind + len(num_next_str) > len(num):
                                terminate = True
                                break
                            if num_next_str == num[ind:(ind + len(num_next_str))]:
                                prev1, prev2 = prev2, num_next
                                ind = ind + len(num_next_str)
                            else:
                                terminate = True
                                break
                        if not terminate:
                            return True
        return False
