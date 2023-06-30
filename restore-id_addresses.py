# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.


class Solution:
    def check_part(self, part):
        if len(part) > 1:
            if part[0] == "0":
                return False
        if int(part) > 255:
            return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []
        results = []
        for i in range(3):
            if i + 3 >= len(s):
                continue
            for j in range(i+1, i+4):
                if j + 2 >= len(s):
                    continue
                for k in range(j+1, j+4):
                    if k + 1 >= len(s):
                        continue
                    fourth_part = s[(k+1):]
                    if len(fourth_part) > 3:
                        continue
                    first_part = s[:(i+1)]
                    second_part = s[(i+1):(j+1)]
                    third_part = s[(j+1):(k+1)]
                    if not self.check_part(fourth_part):
                        continue
                    if not self.check_part(third_part):
                        continue
                    if not self.check_part(second_part):
                        continue
                    if not self.check_part(first_part):
                        continue
                    line = first_part + "." + \
                           second_part + "." + \
                           third_part + "." + \
                           fourth_part
                    if line not in results:
                        results.append(line)
        return results
