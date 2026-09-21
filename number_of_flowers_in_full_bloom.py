# You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.
# Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.
import bisect


class Solution:
    def fullBloomFlowers(
        self, flowers: list[list[int]], people: list[int]
    ) -> list[int]:
        start_times = []
        end_times = []
        for flower in flowers:
            start_times.append(flower[0])
            end_times.append(flower[1])
        start_times.sort()
        end_times.sort()
        answers = []
        for person in people:
            ind_start = bisect.bisect_right(start_times, person)
            ind_end = bisect.bisect_left(end_times, person)
            answers.append(max(ind_start - ind_end, 0))
        return answers
