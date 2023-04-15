# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
                                                                                             

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        s_new = s.replace(' ', '')
        if len(s_new) == 0:
            return 0
        key_pos = 0
        for elem in s:
            if elem != ' ':
              break
            key_pos += 1
        s = s[key_pos:]
        if (s == '+') or (s == '-'):
            return 0
        is_negative = (s[0] == '-')
        if (s[0] in '+-'):
            s = s[1:]
        if (s[0] not in '01234567890'):
            return 0
        s = re.sub('\D', '$', s)
        if '$' in s:
            s = s.split('$')
            for elem in s:
                if elem != '':
                    temp_var = elem
                    break
            s = temp_var
        s = float(s)
        if is_negative:
            s = -s
        s = min(s, 2**31 - 1)
        s = max(s, -2**31)
        return round(s)
