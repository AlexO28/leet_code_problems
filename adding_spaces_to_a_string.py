# You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.
# For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
# Return the modified string after the spaces have been added.
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        ind2 = 0
        for ind1 in range(len(s)):
            if ind2 < len(spaces):
                if ind1 == spaces[ind2]:
                    res.append(" ")
                    ind2 += 1
            res.append(s[ind1])
        return "".join(res)