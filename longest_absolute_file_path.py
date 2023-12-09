# Given a string input representing the file system in the explained format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        lines = input.split("\n")
        cur_path = []
        for line in lines:
            terminate = False
            number_of_tabspaces = 0
            while not terminate:
                if line[0] == "\t":
                    line = line[1:]
                    number_of_tabspaces += 1
                else:
                    terminate = True
            cur_path = cur_path[:number_of_tabspaces]
            cur_path.append(line)
            if "." in line:
                max_len = max(max_len, len("/".join(cur_path)))
        return max_len
   
