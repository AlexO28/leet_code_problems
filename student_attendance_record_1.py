# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.
class Solution:
    def checkRecord(self, s: str) -> bool:
        number_of_absences = 0
        number_of_lates = 0
        for elem in s:
            if elem == "A":
                number_of_absences += 1
                if number_of_absences == 2:
                    return False
                number_of_lates = 0
            elif elem == "L":
                number_of_lates += 1
                if number_of_lates == 3:
                    return False
            else:
                number_of_lates = 0
        return True
 
