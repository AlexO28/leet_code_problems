# Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.
# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.
# A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
# 1 <= xi.length <= 4
# xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
# Leading zeros are allowed in xi.
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.isIPv4(queryIP):
            return "IPv4"
        if self.isIPv6(queryIP):
            return "IPv6"
        return "Neither"

    def isIPv4(self, query):
        nums = query.split(".")
        if len(nums) != 4:
            return False
        for num in nums:
            try:
                num_int = int(num)
            except:
                return False
            if len(str(num_int)) != len(num):
                return False
            if num_int > 255:
                return False
        return True

    def isIPv6(self, query):
        nums = query.split(":")
        if len(nums) != 8:
            return False
        for num in nums:
            if len(num) == 0:
                return False
            if len(num) > 4:
                return False
            try:
                int(num.upper(), 16)
            except:
                return False
        return True
