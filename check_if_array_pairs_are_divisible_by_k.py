# Given an array of integers arr of even length n and an integer k.
# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
# Return true If you can find a way to do that or false otherwise.
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq_dict = {}
        for num in arr:
            remainder = num % k
            if remainder in freq_dict:
                freq_dict[remainder] += 1
            else:
                freq_dict[remainder] = 1
        for i in freq_dict.keys():
            if i == 0:
                if freq_dict[0] % 2 == 1:
                    return False
            else:
                i_prime = k-i
                if i_prime == i:
                    if freq_dict[i] % 2 == 1:
                        return False
                else:
                    if i_prime not in freq_dict.keys():
                        return False
                    if freq_dict[i] != freq_dict[i_prime]:
                        return False
        return True
