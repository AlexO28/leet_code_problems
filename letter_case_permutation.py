# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. Return the output in any order.
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        return self.parseString(s)

    def parseString(self, s):
        if len(s) == 1:
            if s[0].isdigit():
                return [s]
            else:
                return [s.lower(), s.upper()]
        if s[0].isdigit():
            answers = self.parseString(s[1:])
            new_answers = []
            for answer in answers:
                new_answers.append(s[0] + answer)
            return new_answers
        else:
            answers = self.parseString(s[1:])
            new_answers = []
            for answer in answers:
                new_answers.append(s[0].lower() + answer)
                new_answers.append(s[0].upper() + answer)
            return new_answers
