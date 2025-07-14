# Given the array restaurants where  restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]. You have to filter the restaurants using three filters.\
# The veganFriendly filter will be either true (meaning you should only include restaurants with veganFriendlyi set to true) or false (meaning you can include any restaurant). In addition, you have the filters maxPrice and maxDistance which are the maximum value for price and distance of restaurants you should consider respectively.
# Return the array of restaurant IDs after filtering, ordered by rating from highest to lowest. For restaurants with the same rating, order them by id from highest to lowest. For simplicity veganFriendlyi and veganFriendly take value 1 when it is true, and 0 when it is false.
from typing import List


class Solution:
    def filterRestaurants(
        self,
        restaurants: List[List[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int,
    ) -> List[int]:
        res = []
        for restaurant in restaurants:
            if veganFriendly == 1:
                if (
                    (restaurant[2] == veganFriendly)
                    and (restaurant[3] <= maxPrice)
                    and (restaurant[4] <= maxDistance)
                ):
                    res.append(restaurant)
            else:
                if (restaurant[3] <= maxPrice) and (restaurant[4] <= maxDistance):
                    res.append(restaurant)
        res.sort(key=lambda x: (x[1], x[0]), reverse=True)
        return [elem[0] for elem in res]
