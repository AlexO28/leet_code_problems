# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
from random import randint

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        return random.randint(1, 10)
