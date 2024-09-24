# You are given two arrays with positive integers arr1 and arr2.
# A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. For example, 123 is a prefix of the integer 12345, while 234 is not.
# A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b. For example, 5655359 and 56554 have a common prefix 565 while 1223 and 43456 do not have a common prefix.
# You need to find the length of the longest common prefix between all pairs of integers (x, y) such that x belongs to arr1 and y belongs to arr2.
# Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_dict = {}
        for elem in arr1:
            elem = str(elem)
            for j in range(1, len(elem)+1):
                if elem[:j] not in prefix_dict:
                    prefix_dict[elem[:j]] = 1
        max_len = 0
        for elem in arr2:
            elem = str(elem)
            for j in range(1, len(elem)+1):
                if elem[:j] in prefix_dict:
                    max_len = max(max_len, j)
        return max_len
