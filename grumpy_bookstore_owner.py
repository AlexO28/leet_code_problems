# There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
# On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
# Return the maximum number of customers that can be satisfied throughout the day.
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_economy = 0
        happy_anyway = 0
        i = 0
        ii = minutes-1
        cur_economy = 0
        while ii < len(customers):
            if i == 0:
                for j in range(ii+1):
                    if grumpy[j] == 0:
                        happy_anyway += customers[j]
                    else:
                        cur_economy += customers[j]
            else:
                happy_anyway +=  customers[ii]*(1-grumpy[ii])
                cur_economy += customers[ii]*grumpy[ii] - customers[i-1]*grumpy[i-1]
            max_economy = max(max_economy, cur_economy)
            i += 1
            ii += 1 
        return max_economy + happy_anyway
