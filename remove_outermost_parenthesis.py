# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        num_open = 0
        num_close = 0
        line = []
        for i in range(len(s)):
            if s[i] == "(":
                num_open += 1
            else:
                num_close += 1
            if num_open == num_close:
                if len(line) > 1:
                    print(line)
                    line = "".join(line[1:])
                    res.append(line)
                line = []
            else:
                line.append(s[i])
        return "".join(res)
