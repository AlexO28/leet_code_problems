class Solution:
    def reverseParentheses(self, s: str) -> str:
        self.s = "((" + s + "))"
        res, pos = self.__findWithReverse(0)
        return res

    def __findWithReverse(self, ind):
        res = []
        temp_res = []
        i = ind+1
        while i < len(self.s):
            if self.s[i] == "(":
                ret_res, fin = self.__findWithReverse(i)
                i = fin
                temp_res.extend(ret_res)
            elif self.s[i] == ")":
                res.extend(temp_res[::-1])
                i += 1
                break
            else:
                temp_res.append(self.s[i])
                i += 1
        return "".join(res), i
