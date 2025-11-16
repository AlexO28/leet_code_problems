# You are given a string num representing the digits of a very large integer and an integer k. You are allowed to swap any two adjacent digits of the integer at most k times.
# Return the minimum integer you can obtain also as a string.
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        min_num = sorted(list(num))
        min_num = "".join(min_num)
        i = 0
        to_find = 0
        while num != min_num and k > 0 and i < len(num):
            indx = num.find(str(to_find), i)
            while indx != -1:
                if indx - i <= k:
                    num = num[:i] + num[indx] + num[i:indx] + num[indx + 1 :]
                    k -= indx - i
                    i += 1
                    to_find = 0
                    indx = num.find(str(to_find), i)
                else:
                    break
            to_find += 1
        return num
