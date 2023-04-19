# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        queue_brackets = []
        for elem in s:
            if (elem == '(') or (elem == '[') or (elem == '{'):
                queue_brackets.append(elem)
            elif (elem == ')') or (elem == ']') or (elem == '}'):
                if len(queue_brackets) == 0:
                    return False
                if elem == ')':
                    last_elem = queue_brackets.pop()
                    if last_elem != '(':
                        return False
                elif elem == ']':
                    last_elem = queue_brackets.pop()
                    if last_elem != '[':
                        return False
                elif elem == '}':
                    last_elem = queue_brackets.pop()
                    if last_elem != '{':
                        return False
        if len(queue_brackets) > 0:
            return False    
        return True
 
