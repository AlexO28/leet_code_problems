# We define str = [s, n] as the string str which consists of the string s concatenated n times.
# For example, str == ["abc", 3] =="abcabcabc".
# We define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1.
# For example, s1 = "abc" can be obtained from s2 = "abdbec" based on our definition by removing the bolded underlined characters.
# You are given two strings s1 and s2 and two integers n1 and n2. You have the two strings str1 = [s1, n1] and str2 = [s2, n2].
# Return the maximum integer m such that str = [str2, m] can be obtained from str1.
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        repetition_dict = {}
        for i in range(len(s2)):
            number_of_repetitions = 0
            j = i
            for elem in s1:
                if elem == s2[j]:
                    j += 1
                if j == len(s2):
                    number_of_repetitions += 1
                    j = 0
            repetition_dict[i] = (number_of_repetitions, j) 
        total_number_of_repetitions = 0
        target_index = 0
        for i in range(n1):
            number_of_repetitions, target_index = repetition_dict[target_index]
            total_number_of_repetitions += number_of_repetitions
        return total_number_of_repetitions // n2
