# We have two special characters:
# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        codes = []
        search_zero = True
        for bit in bits:
            if search_zero:
                if bit == 0:
                    codes.append(0)
                else:
                    codes.append(1)
                    search_zero = False
            else:
                search_zero = True
        return codes[-1] == 0
