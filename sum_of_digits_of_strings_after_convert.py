# You are given a string s consisting of lowercase English letters, and an integer k.
# First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.
# Return the resulting integer after performing the operations described above.
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = "".join([str(ord(elem) - ord("a") + 1) for elem in s])
        while k > 0:
            num = sum([int(elem) for elem in list(str(num))])
            if num < 10:
                return num
            k -= 1
        return num
