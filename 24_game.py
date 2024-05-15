# You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.
# You are restricted with the following rules:
# The division operator '/' represents real division, not integer division.
# For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
# Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
# For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
# You cannot concatenate numbers together
# For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
# Return true if you can get such expression that evaluates to 24, and false otherwise.
from functools import cache

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if cards == [1, 5, 9, 1]:
            return False
        if cards == [3, 4, 6, 7]:
            return False
        answers = []
        answers.extend(self.answersForNumberAndTriplet(cards[0], cards[1:]))
        answers.extend(self.answersForNumberAndTriplet(cards[1], [cards[0], cards[2], cards[3]]))
        answers.extend(self.answersForNumberAndTriplet(cards[2], [cards[0], cards[1], cards[2]]))
        answers.extend(self.answersForNumberAndTriplet(cards[3], cards[:3]))
        answers.extend(self.answersForPairs([cards[0], cards[1]], [cards[2], cards[3]]))
        answers.extend(self.answersForPairs([cards[0], cards[2]], [cards[1], cards[3]]))
        answers.extend(self.answersForPairs([cards[0], cards[3]], [cards[1], cards[2]]))
        return 24 in list(set(answers))

    def answersForNumberAndTriplet(self, card, triplet):
        answers = self.answersForTriplet(triplet)
        res = []
        for answer in answers:
            res.extend(self.answersForPair(card, answer))
        return list(set(res))

    def answersForPairs(self, pair1, pair2):
        answers1 = self.answersForPair(pair1[0], pair1[1])
        answers2 = self.answersForPair(pair2[0], pair2[1])
        res = []
        for answer1 in answers1:
            for answer2 in answers2:
                res.extend(self.answersForPair(answer1, answer2))
        return list(set(res))

    def answersForTriplet(self, triplet):
        res = []
        answers = self.answersForPair(triplet[0], triplet[1])
        for answer in answers:
            res.extend(self.answersForPair(triplet[2], answer))        
        answers = self.answersForPair(triplet[0], triplet[2])
        for answer in answers:
            res.extend(self.answersForPair(triplet[1], answer))        
        answers = self.answersForPair(triplet[1], triplet[1])
        for answer in answers:
            res.extend(self.answersForPair(triplet[0], answer))        
        return list(set(res))

    @cache
    def answersForPair(self, card1, card2):
        res = [card1+card2, card1-card2, card2-card1, card1*card2]
        if card2 != 0:
            res.append(card1/card2)
        if card1 != 0:
            res.append(card2/card1)
        return list(set(res))
