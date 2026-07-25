# A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).
# You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:
# Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
# Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(self.count("T", answerKey, k), self.count("F", answerKey, k))

    def count(self, c, answerKey, k):
        cnt = 0
        l = 0
        for ch in answerKey:
            cnt += ch == c
            if cnt > k:
                cnt -= answerKey[l] == c
                l += 1
        return len(answerKey) - l
