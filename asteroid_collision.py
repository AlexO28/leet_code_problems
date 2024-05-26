# We are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        positives = []
        negatives = []
        start = True
        skipped = []
        for asteroid in asteroids:
            if start:
                if asteroid > 0:
                    start = False
                    positives.append(asteroid)
                else:
                    skipped.append(asteroid)
            else:
                if asteroid > 0:
                    positives.append(asteroid)
                else:
                    negatives.append(asteroid)
                while (len(positives) > 0) and (len(negatives) > 0):
                    positive = positives.pop()
                    negative = negatives.pop()
                    if positive > -negative:
                        positives.append(positive)
                    elif positive < -negative:
                        negatives.append(negative)
                if len(negatives) > 0:
                    skipped.extend(negatives)
                    negatives = []
        if len(positives) > 0:
            skipped.extend(positives)
        else:
            skipped.extend(negatives)    
        return skipped
