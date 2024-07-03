# You are given an integer array arr.
# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
# Return the largest number of chunks we can make to sort the array.
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for value in arr:
            if (len(stack) == 0) or (value >= stack[-1]):
                stack.append(value)
            else:
                max_in_chunk = stack.pop()
                while (len(stack) > 0) and (stack[-1] > value):
                    stack.pop()
                stack.append(max_in_chunk)
        return len(stack)
