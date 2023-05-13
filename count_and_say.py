# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.


class Solution:
    def countAndSay(self, n: int) -> str:
        prev_number = 1
        for j in range(1, n+1):
            if j == 1:
                cur_number = 1
            else:
                str_repr = str(prev_number)
                prev_symb = ""
                cur_number = ""
                count = 0
                for symb in str_repr:
                    if symb != prev_symb:
                        if (prev_symb != ""):
                            cur_number += str(count + 1)
                            cur_number += prev_symb
                        prev_symb = symb
                        count = 0
                    else:
                        count += 1
                cur_number += str(count + 1)
                cur_number += symb
                prev_number = cur_number
        return str(cur_number)
  
