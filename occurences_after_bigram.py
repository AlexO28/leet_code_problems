# Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.
# Return an array of all the words third for each occurrence of "first second third".
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split(" ")
        res = []
        for j in range(2, len(words)):
            if (words[j-2] == first) and (words[j-1] == second):
                res.append(words[j])
        return res
