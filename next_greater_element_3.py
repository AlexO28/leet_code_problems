# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.
# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_list = [int(d) for d in list(str(n))]
        if len(n_list) == 1:
            return -1
        i = len(n_list) - 2
        while i >= 0 and n_list[i] >= n_list[i + 1]:
            i -= 1
        if i < 0:
            return -1      
        j = len(n_list) - 1
        while n_list[i] >= n_list[j]:
            j -= 1
        n_list[i], n_list[j] = n_list[j], n_list[i]      
        n_list[i+1 :] = n_list[i+1:][::-1]
        next_greater = int(''.join([str(d) for d in n_list]))
        if next_greater <= 2**31 - 1:
            return next_greater
        else:
            return -1
