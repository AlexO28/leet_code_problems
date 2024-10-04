# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.
# Return true if and only if we can do this so that the resulting number is a power of two.
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        freq_count = {}
        for elem in list(str(n)):
            elem = int(elem)
            if elem in freq_count:
                freq_count[elem] += 1
            else:
                freq_count[elem] = 1
        cur_num = 1
        max_num = 10 ** 9
        while (cur_num < max_num) and (len(str(cur_num)) <= len(str(n))):
            new_freq_count = {}
            found = True
            for elem in list(str(cur_num)):
                elem = int(elem)
                if elem not in freq_count:
                    found = False
                    break
                if elem in new_freq_count:
                    new_freq_count[elem] += 1
                else:
                    new_freq_count[elem] = 1
            if found:
                for digit in freq_count:
                    if digit not in new_freq_count:
                        found = False
                        break
                    else:
                        if new_freq_count[digit] != freq_count[digit]:
                            found = False
                            break
            if found:
                return True
            else:
                cur_num *= 2
        return False
