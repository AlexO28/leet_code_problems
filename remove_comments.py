# Given a C++ program, remove comments from it. The program source is an array of strings source where source[i] is the ith line of the source code. This represents the result of splitting the original source code string by the newline character '\n'.
# In C++, there are two types of comments, line comments, and block comments.
# The string "//" denotes a line comment, which represents that it and the rest of the characters to the right of it in the same line should be ignored.
# The string "/*" denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of "*/" should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string "/*/" does not yet end the block comment, as the ending would be overlapping the beginning.
# The first effective comment takes precedence over others.
# For example, if the string "//" occurs in a block comment, it is ignored.
# Similarly, if the string "/*" occurs in a line or block comment, it is also ignored.
# If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.
# There will be no control characters, single quote, or double quote characters.
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        sink = []
        comment_started_multiline = False
        res_line = []
        for line in source:
            if len(line) <= 1:
                if not comment_started_multiline:
                    sink.append("".join(line))
                else:
                    erased_something = True
            else:
                erased_something = False
                i = 0
                while i < len(line):
                    if i < len(line) - 1:
                        if (line[i] == "/") and (line[i+1] == "/"):
                            if not comment_started_multiline:
                                erased_something = True
                                break
                            else:
                                erased_something = True
                                i += 1
                        elif (line[i] == "*") and (line[i+1] == "/"):
                            if comment_started_multiline:
                                comment_started_multiline = False
                                erased_something = True
                                i += 2
                            else:
                                res_line.append("*")
                                i += 1
                        elif (line[i] == "/") and (line[i+1] == "*"):
                            if not comment_started_multiline:
                                comment_started_multiline = True
                                erased_something = True
                                i += 2
                            else:
                                erased_something = True
                                i += 1
                        else:
                            if not comment_started_multiline:
                                res_line.append(line[i])
                            else:
                                erased_something = True
                            i += 1
                    else:
                        if not comment_started_multiline:
                            res_line.append(line[i])
                        else:
                            erased_something = True
                        i += 1                        
                if not comment_started_multiline:
                    if erased_something:
                        if len(res_line) > 0:
                            sink.append("".join(res_line))
                    else:
                        sink.append("".join(res_line))
                    res_line = []
        return sink
