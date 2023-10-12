# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

# Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        visit = set()
        q = []
        temp = 0
        level = False
        q.append(s)
        visit.add(s)
        while(len(q)):
            s = q[0]
            q.pop(0)
            if (self.isValidString(s)):
                res.append(s)
                level = True
            if level:
                continue
            for i in range(len(s)):
                if (not self.isParenthesis(s[i])):
                    continue
                temp = s[0:i] + s[i+1:] 
                if temp not in visit:
                    q.append(temp)
                    visit.add(temp)
        return res

    def isParenthesis(self, symb):
        return ((symb == '(') or (symb == ')')) 

    def isValidString(self, line):
        count = 0
        for i in range(len(line)):
            if (line[i] == '('):
                count += 1
            elif (line[i] == ')'):
                count -= 1
            if (count < 0):
                return False
        return (count == 0)
