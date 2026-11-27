# Given four integers length, width, height, and mass, representing the dimensions and mass of a box, respectively, return a string representing the category of the box.
# The box is "Bulky" if:
# Any of the dimensions of the box is greater or equal to 104.
# Or, the volume of the box is greater or equal to 109.
# If the mass of the box is greater or equal to 100, it is "Heavy".
# If the box is both "Bulky" and "Heavy", then its category is "Both".
# If the box is neither "Bulky" nor "Heavy", then its category is "Neither".
# If the box is "Bulky" but not "Heavy", then its category is "Bulky".
# If the box is "Heavy" but not "Bulky", then its category is "Heavy".
# Note that the volume of the box is the product of its length, width and height.
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_bulky = False
        is_heavy = False
        if (length >= 10000) or (width >= 10000) or (height >= 10000):
            is_bulky = True
        elif length * width * height >= 1000000000:
            is_bulky = True
        if mass >= 100:
            is_heavy = True
        if is_bulky and is_heavy:
            return "Both"
        elif not is_bulky and not is_heavy:
            return "Neither"
        elif is_bulky:
            return "Bulky"
        else:
            return "Heavy"
