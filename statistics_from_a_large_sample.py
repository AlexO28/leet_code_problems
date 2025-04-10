# You are given a large sample of integers in the range [0, 255]. Since the sample is so large, it is represented by an array count where count[k] is the number of times that k appears in the sample.
# Calculate the following statistics:
# minimum: The minimum element in the sample.
# maximum: The maximum element in the sample.
# mean: The average of the sample, calculated as the total sum of all elements divided by the total number of elements.
# median:
# If the sample has an odd number of elements, then the median is the middle element once the sample is sorted.
# If the sample has an even number of elements, then the median is the average of the two middle elements once the sample is sorted.
# mode: The number that appears the most in the sample. It is guaranteed to be unique.
# Return the statistics of the sample as an array of floating-point numbers [minimum, maximum, mean, median, mode]. Answers within 10-5 of the actual answer will be accepted.
from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        for j in range(len(count)):
            if count[j] > 0:
                min_val = j
                break
        for j in range(len(count)-1, -1, -1):
            if count[j] > 0:
                max_val = j
                break
        summa = 0
        num = 0
        max_count = 0
        for j in range(len(count)):
            if count[j] > 0:
                summa += j * count[j]
                num += count[j]
                max_count = max(max_count, count[j])
        mean_val = summa/num
        for j in range(len(count)):
            if count[j] == max_count:
                mode_val = j
                break
        main_part, remainder = divmod(num, 2)
        if remainder == 1:
            curpart = 0
            for j in range(len(count)):
                if count[j] > 0:
                    if curpart + count[j] > main_part:
                        med_val = j
                        break
                    curpart += count[j]
        else:
            curpart = 0
            first_num = None
            for j in range(len(count)):
                if count[j] > 0:
                    if first_num is None:
                        if curpart + count[j] >= main_part:
                            first_num = j
                    if first_num is not None:
                        if curpart + count[j] > main_part:
                            second_num = j
                            break
                    curpart += count[j]
            med_val = (first_num + second_num)/2
        return min_val, max_val, mean_val, med_val, mode_val
