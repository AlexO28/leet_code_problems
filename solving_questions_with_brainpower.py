# You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].
# The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.
# Return the maximum points you can earn for the exam.
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        answers = [0] * (len(questions) + 1)
        for j in range(len(questions) - 1, -1, -1):
            answers[j] = max(
                answers[j + 1],
                questions[j][0] + answers[min(j + 1 + questions[j][1], len(questions))],
            )
        return answers[0]
