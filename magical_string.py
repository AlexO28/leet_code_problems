# A magical string s consists of only '1' and '2' and obeys the following rules:
# The string s is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string s itself.
# The first few elements of s is s = "1221121221221121122……". If we group the consecutive 1's and 2's in s, it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......" and the occurrences of 1's or 2's in each group are "1 2 2 1 1 2 1 2 2 1 2 2 ......". You can see that the occurrence sequence is s itself.
# Given an integer n, return the number of 1's in the first n number in the magical string s.
class Solution:
    def magicalString(self, n: int) -> int:
        if n == 1:
            return 1
        res = [1, 2, 2]
        ind = 2   
        while len(res) < n:
            if res[-1] == 2:
                next_elem = 1
            else:
                next_elem = 2
            if res[ind] == 1:
                res.append(next_elem)
            else:
                res.append(next_elem)
                res.append(next_elem)
            ind += 1
        res = res[:n]
        return len([r for r in res if r == 1])
        
