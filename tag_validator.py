# Given a string representing a code snippet, implement a tag validator to parse the code and return whether it is valid.
# A code snippet is valid if all the following rules hold:
# The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
# A closed tag (not necessarily valid) has exactly the following format : <TAG_NAME>TAG_CONTENT</TAG_NAME>. Among them, <TAG_NAME> is the start tag, and </TAG_NAME> is the end tag. The TAG_NAME in start and end tags should be the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.
# A valid TAG_NAME only contain upper-case letters, and has length in range [1,9]. Otherwise, the TAG_NAME is invalid.
# A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1) EXCEPT unmatched <, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is invalid.
# A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.
# A < is unmatched if you cannot find a subsequent >. And when you find a < or </, all the subsequent characters until the next > should be parsed as TAG_NAME (not necessarily valid).
# The cdata has the following format : <![CDATA[CDATA_CONTENT]]>. The range of CDATA_CONTENT is defined as the characters between <![CDATA[ and the first subsequent ]]>.
# CDATA_CONTENT may contain any characters. The function of cdata is to forbid the validator to parse CDATA_CONTENT, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as regular characters.
class Solution:
    def isValid(self, code: str) -> bool:
        if code[0] != '<' or code[-1] != '>':
            return False
        self.containsTag = False
        self.stack = []
        i = 0
        while i < len(code):
            if not self.stack and self.containsTag:
                return False
            if code[i] == '<':
                if self.stack and code[i + 1] == '!':
                    closeIndex = code.find(']]>', i + 2)
                    if closeIndex == -1 or not self.isValidCdata(code[i + 2:closeIndex]):
                        return False
                elif code[i + 1] == '/':
                    closeIndex = code.find('>', i + 2)
                    if closeIndex == -1 or not self.isValidTagName(code[i + 2:closeIndex], True):
                        return False
                else:
                    closeIndex = code.find('>', i + 1)
                    if closeIndex == -1 or not self.isValidTagName(code[i + 1:closeIndex], False):
                        return False
                i = closeIndex
            i += 1
        return not self.stack and self.containsTag

    def isValidCdata(self, s):
        return s.find('[CDATA[') == 0

    def isValidTagName(self, tagName, isEndTag):
        if not tagName or len(tagName) > 9:
            return False
        for c in tagName:
            if not c.isupper():
                return False
        if isEndTag:
            return self.stack and self.stack.pop() == tagName
        self.containsTag = True
        self.stack.append(tagName)
        return True
