# You are given a string s of lowercase English letters and an integer array shifts of the same length.
# Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').
# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
# Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.
# Return the final string after all such shifts to s are applied.
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        accum_shifts = []
        total_shift = 0
        for j in range(len(shifts)-1, -1, -1):
            total_shift += shifts[j]
            accum_shifts.append(total_shift % 26)
        accum_shifts = accum_shifts[::-1] 
        res = []
        for j in range(len(accum_shifts)):
            res.append(chr(((ord(s[j]) - ord("a") + accum_shifts[j]) % 26) + ord("a")))
        return "".join(res)
