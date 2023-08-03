# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        candies = [1]*len(ratings)
        for j in range(1, len(ratings)):
            if ratings[j] > ratings[j - 1]:
                candies[j] = candies[j - 1] + 1 
        for j in range(1, len(ratings)):
            if ratings[len(ratings)-j] < ratings[len(ratings)-j-1]:
               candies[len(ratings)-j-1] = max(candies[len(ratings)-j] + 1, candies[len(ratings)-j-1]) 
        return sum(candies)
