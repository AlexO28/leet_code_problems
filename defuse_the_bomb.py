# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)
        elif k > 0:
            if len(code) == 1:
                return code
            n = len(code)
            code.extend(code)
            res = []
            start = 1
            end = k+1
            summa = sum([code[j] for j in range(start, end)])
            res.append(summa)
            for j in range(1, n):
                summa -= code[start]
                summa += code[end]
                start += 1
                end += 1
                res.append(summa)
            return res
        else:
            if len(code) == 1:
                return code
            n = len(code)
            code.extend(code)
            start = n+k
            end = n
            res = []
            summa = sum([code[j] for j in range(start, end)])
            res.append(summa)
            for j in range(1, n):
                summa += code[end]
                summa -= code[start]
                start += 1
                end += 1
                res.append(summa)
            return res
