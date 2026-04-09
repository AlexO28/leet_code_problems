# You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.
# For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain the keys "name" and "age".
# You know the values of a wide range of keys. This is represented by a 2D string array knowledge where each knowledge[i] = [keyi, valuei] indicates that key keyi has a value of valuei.
# You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains some key keyi, you will:
# Replace keyi and the bracket pair with the key's corresponding valuei.
# If you do not know the value of the key, you will replace keyi and the bracket pair with a question mark "?" (without the quotation marks).
# Each key will appear at most once in your knowledge. There will not be any nested brackets in s.
# Return the resulting string after evaluating all of the bracket pairs.
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_dict = {}
        for key, value in knowledge:
            knowledge_dict[key] = value
        s = list(s)
        new_s = []
        temp = []
        add_to_temp = False
        for elem in s:
            if elem == "(":
                add_to_temp = True
            elif elem == ")":
                add_to_temp = False
                temp = "".join(temp)
                if temp in knowledge_dict:
                    new_s.append(knowledge_dict[temp])
                else:
                    new_s.append("?")
                temp = []
            else:
                if add_to_temp:
                    temp.append(elem)
                else:
                    new_s.append(elem)
        return "".join(new_s)
